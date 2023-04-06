import asyncio
import Utils

if __name__ == "__main__":
    Utils.init_logging("PizzaTowerClient", exception_logger="Client")

from CommonClient import ClientCommandProcessor, CommonContext, server_loop, gui_enabled, get_base_parser


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
        self.game = "Pizza Tower"
        self.got_deathlink = False
        self.syncing = False

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

