from BaseClasses import Tutorial
from .Rules import set_rules
from ..AutoWorld import World, WebWorld
from .Options import PizzaTowerOptions
from .Items import item_table, PizzaTowerItem, toppin_table, pumpkin_table, treasure_table
from .Locations import PizzaTowerLocation, location_table
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
    options_dataclass = PizzaTowerOptions
    options: PizzaTowerOptions
    web = PizzaTowerWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in location_table.items()}

    data_version = 0

    required_client_version = (0, 4, 6)

    item_name_groups = {
        "toppins": set(toppin_table.keys()),
        "treasures": set(treasure_table.keys()),
        "pumpkins": set(pumpkin_table.keys())
    }

    def fill_slot_data(self):
        return {
            "death_link": self.options.death_link.value,
            "treasure_check": self.options.treasure_check.value,
            "secret_eye_check": self.options.secret_eye_check.value,
            "pumpkin_hunt": self.options.pumpkin_hunt.value,
            "shuffle_level": self.options.shuffle_level.value,
            "rank_needed": self.options.rank_needed.value,
            "goal": self.options.goal.value,
            "john": self.options.john.value
        }

    def create_item(self, name: str) -> PizzaTowerItem:
        return Items.create_item(self.multiworld, name, self.player, self.options)

    def create_regions(self) -> None:
        create_regions(self.multiworld, self.player, self.options)

    def create_items(self) -> None:
        Items.create_all_items(self.multiworld, self.player, self.options)

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player, self.options)

    def generate_basic(self) -> None:
        world = self.multiworld
        victory_item = world.create_item("Victory", self.player)
        self.multiworld.get_location("Escape " + tower, self.player).place_locked_item(victory_item)

        if self.options.boss_keys.value == 0:
            pepperman_key = world.create_item(pepperman + " Boss Key", self.player)
            self.multiworld.get_location("Defeat " + pepperman, self.player).place_locked_item(pepperman_key)
            vigilante_key = world.create_item(vigilante + " Boss Key", self.player)
            self.multiworld.get_location("Defeat " + vigilante, self.player).place_locked_item(vigilante_key)
            noise_key = world.create_item(noise + " Boss Key", self.player)
            self.multiworld.get_location("Defeat " + noise, self.player).place_locked_item(noise_key)
            fakepep_key = world.create_item(fakepep + " Boss Key", self.player)
            self.multiworld.get_location("Defeat " + fakepep, self.player).place_locked_item(fakepep_key)
