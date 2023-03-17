from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Entrance, Region
from .Regions import tower_regions
from .Rules import set_rules
from ..AutoWorld import World, WebWorld
from .Options import pizza_tower_options
from .Items import item_table, PizzaTowerItem, toppin_table
from .Locations import task_table, PizzaTowerTask
from . import Options, Items, Locations, Regions, Rules, Names


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
    topology_present = True
    web = PizzaTowerWeb()

    item_name_to_id = {name: data.code for name, data in item_table.items()}
    location_name_to_id = {name: data.id for name, data in task_table.items()}

    data_version = 0

    # required_client_version = (1, 0, 311)

    item_name_groups = {
        "toppins": toppin_table.keys()
    }

    def get_option(self, name):
        return getattr(self.multiworld, name)[self.player].value

    def fill_slot_data(self):
        slot_data = {
            "seed": self.multiworld.seed_name,
            "level_shuffle": self.multiworld.shuffle_level[self.player].value,
            "rank_needed": self.multiworld.rank_needed[self.player].value,
            "judgement": self.multiworld.goal[self.player].value,
            "john": self.multiworld.john[self.player].value,
            "death_link": self.multiworld.death_link[self.player].value,
        }

        for option_name in self.option_definitions:
            slot_data[option_name] = self.get_option(option_name)

        return slot_data

    def create_item(self, name: str) -> PizzaTowerItem:
        item_data = item_table[name]
        if item_data.required:
            classification = ItemClassification.progression
        elif item_data.toppin:
            classification = ItemClassification.progression_skip_balancing
        elif item_data.trap:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
        item = PizzaTowerItem(name, classification, item_data.code, self.player)
        return item

    def create_regions(self) -> None:
        def TowerRegion(region_name: str, exits=[]):
            ret = Region(region_name, self.player, self.multiworld)
            ret.locations = [PizzaTowerTask(self.player, loc_name, loc_data.id, ret)
                             for loc_name, loc_data in task_table.items()
                             if loc_data.region == region_name]
            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.multiworld.regions += [TowerRegion(*r) for r in tower_regions]
        Regions.link_tower_structures(self.multiworld, self.player)

    def create_items(self) -> None:
        Items.create_all_items(self.multiworld, self.player)

    def generate_early(self) -> None:
        world = self.multiworld

        victory = self.create_item("Victory")
        world.push_precollected(victory)

    def generate_basic(self) -> None:
        world = self.multiworld

        victory = self.create_item("Victory")
        world.get_location("Escape " + Names.tower, self.player).place_locked_item(victory)

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player)
