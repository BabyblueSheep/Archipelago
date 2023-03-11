from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from ..AutoWorld import World, WebWorld
from .Options import pizza_tower_options
from .Items import item_table, PizzaTowerItem
from .Locations import task_table
from . import Options, Items, Locations, Regions, Rules


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
    """Pizza Tower is a fast-paced 2D platformer inspired by the Wario Land series, in which you progress through levels
    in the titular Pizza Tower, incorporating a tight combo system, multiple types of collectibles, escape sequences, and bosses."""

    game: str = "Pizza Tower"
    option_definitions = pizza_tower_options
    topology_present = False
    web = PizzaTowerWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in task_table.items()}

    data_version = 1

    def get_option(self, name):
        return getattr(self.multiworld, name)[self.player].value

    def fill_slot_data(self):
        slot_data = {
            "seed": self.multiworld.seed_name,
            "death_link": self.multiworld.death_link[self.player].value,
        }

        for option_name in self.option_definitions:
            slot_data[option_name] = self.get_option(option_name)

        return slot_data

    def create_regions(self) -> None:
        Regions.link_tower_structures(self.multiworld, self.player)

    def create_items(self) -> None:
        Items.create_all_items(self.multiworld, self.player)

