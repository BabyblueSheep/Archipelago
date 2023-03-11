from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification
from ..AutoWorld import World, WebWorld
from .Options import pizza_tower_options
from .Items import item_table, PizzaTowerItem
from .Locations import task_table


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
# test

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

    def create_item(self, name: str) -> Item:
        item_data = item_table[name]
        if item_data.required:
            classification = ItemClassification.progression
        else:
            classification = ItemClassification.filler
        item = PizzaTowerItem(name, classification, item_data.code, self.player)
        return item
