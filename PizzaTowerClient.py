import asyncio
import os
import shutil
import sys

import Utils
from NetUtils import NetworkItem

if __name__ == "__main__":
    Utils.init_logging("PizzaTowerClient", exception_logger="Client")

from CommonClient import ClientCommandProcessor, CommonContext, server_loop, gui_enabled, get_base_parser, logger


class PizzaTowerCommandProcessor(ClientCommandProcessor):
    def _cmd_resync(self):
        """Manually trigger a resync."""
        self.output(f"Syncing items.")
        self.ctx.syncing = True


class PizzaTowerContext(CommonContext):
    command_processor: int = PizzaTowerCommandProcessor
    game = "Pizza Tower"
    items_handling = 0b111  # full remote

    def __init__(self, server_address, password):
        super().__init__(server_address, password)
        self.got_deathlink = False
        self.syncing = False
        self.awaiting_bridge = False
        # self.game_communication_path: files go in this path to pass data between us and the actual game
        if "localappdata" in os.environ:
            self.game_communication_path = os.path.expandvars(r"%appdata%/PizzaTower_AP/Archipelago")
        else:
            # not windows. game is an exe so let's see if wine might be around to run it
            if "WINEPREFIX" in os.environ:
                wineprefix = os.environ["WINEPREFIX"]
            elif shutil.which("wine") or shutil.which("wine-stable"):
                wineprefix = os.path.expanduser(
                    "~/.wine")  # default root of wine system data, deep in which is app data
            else:
                msg = "PizzaTowerClient couldn't detect system type. Unable to infer required game_communication_path"
                logger.error("Error: " + msg)
                Utils.messagebox("Error", msg, error=True)
                sys.exit(1)
            self.game_communication_path = os.path.join(
                wineprefix,
                "drive_c",
                os.path.expandvars("users/$USER/Local Settings/Application Data/PizzaTower_AP/Archipelago"))

    async def server_auth(self, password_requested: bool = False):
        if password_requested and not self.password:
            await super(PizzaTowerContext, self).server_auth(password_requested)
        await self.get_username()
        await self.send_connect()

    @property
    def endpoints(self):
        if self.server:
            return [self.server]
        else:
            return []

    def on_package(self, cmd: str, args: dict):
        if cmd in {"ReceivedItems"}:
            start_index = args["index"]
            if start_index != len(self.items_received):
                for item in args['items']:
                    filename = f"{str(NetworkItem(*item).item)}{str(self.player_names.get(NetworkItem(*item).player))}.item"
                    open(os.path.join(self.game_communication_path, filename), 'x')

    def run_gui(self):
        """Import kivy UI system and start running it as self.ui_task."""
        from kvui import GameManager

        class PizzaTowerManager(GameManager):
            logging_pairs = [
                ("Client", "Archipelago")
            ]
            base_title = "Archipelago Pizza Tower Client"

        self.ui = PizzaTowerManager(self)
        self.ui_task = asyncio.create_task(self.ui.async_run(), name="UI")


async def game_watcher(ctx: PizzaTowerContext):
    while not ctx.exit_event.is_set():
        if ctx.syncing:
            sync_msg = [{"cmd": "Sync"}]
            await ctx.send_msgs(sync_msg)
            ctx.syncing = False
        if ctx.got_deathlink:
            ctx.got_deathlink = False
        await asyncio.sleep(0.1)


if __name__ == '__main__':
    async def main(args):
        ctx = PizzaTowerContext(args.connect, args.password)
        ctx.server_task = asyncio.create_task(server_loop(ctx), name="server loop")
        if gui_enabled:
            ctx.run_gui()
        ctx.run_cli()
        progression_watcher = asyncio.create_task(
            game_watcher(ctx), name="PizzaTowerProgressionWatcher")

        await ctx.exit_event.wait()
        ctx.server_address = None

        await progression_watcher

        await ctx.shutdown()

    import colorama

    parser = get_base_parser(description="Pizza Tower Client, for text interfacing.")

    args, rest = parser.parse_known_args()
    colorama.init()
    asyncio.run(main(args))
    colorama.deinit()

