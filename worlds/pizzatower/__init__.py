from BaseClasses import Tutorial
from .Rules import set_rules
from ..AutoWorld import World, WebWorld
from .Options import pizza_tower_options
from .Items import item_table, PizzaTowerItem, toppin_table
from .Locations import PizzaTowerLocation, location_table, treasure_table
from . import Options, Items, Locations, Regions, Rules
from .Names import *
from .Regions import create_regions


class PizzaTowerWeb(WebWorld):
    theme = "partyTime"

    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Pizza Tower randomizer connected to an Archipelago Multiworld.",
        "English",
        "setup_en.md",
        "setup/en",
        ["babybluesheep"]
    )
    tutorials = [setup_en]


class PizzaTowerWorld(World):
    """Pizza Tower is a fast-paced 2D platformer inspired by the Wario Land series, in which you progress through
    levels in the titular Pizza Tower, incorporating a tight combo system, multiple types of collectibles,
    escape sequences, and bosses."""

    game = "Pizza Tower"
    option_definitions = pizza_tower_options
    web = PizzaTowerWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in location_table.items()}

    data_version = 0

    required_client_version = (0, 3, 9)

    item_name_groups = {
        "toppins": set(toppin_table.keys()),
        "treasures": set(treasure_table.keys())
    }

    def get_option(self, name):
        return getattr(self.multiworld, name)[self.player].value

    def fill_slot_data(self):
        slot_data = {}

        for option_name in self.option_definitions:
            slot_data[option_name] = self.get_option(option_name)

        return slot_data

    def create_item(self, name: str) -> PizzaTowerItem:
        return Items.create_item(self.multiworld, name, self.player)

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player)

    def create_items(self) -> None:
        Items.create_all_items(self.multiworld, self.player)

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player)

    def generate_basic(self) -> None:
        world = self.multiworld
        victory_item = world.create_item("Victory", self.player)
        self.multiworld.get_location("Escape " + Names.tower, self.player).place_locked_item(victory_item)

        if world.boss_keys[self.player].value == 0:
            pepperman_key = world.create_item(pepperman + " Boss Key", self.player)
            self.multiworld.get_location("Defeat " + Names.pepperman, self.player).place_locked_item(pepperman_key)
