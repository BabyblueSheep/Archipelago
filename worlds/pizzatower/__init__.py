from BaseClasses import Item, MultiWorld, Tutorial, ItemClassification, Entrance, Region
from .Regions import tower_regions
from .Rules import set_rules
from ..AutoWorld import World, WebWorld
from .Options import pizza_tower_options
from .Items import item_table, PizzaTowerItem, toppin_table
from .Locations import PizzaTowerTask, location_table, treasure_table
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
    location_name_to_id = {name: data.id for name, data in location_table.items()}

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
            "boss_keys": self.multiworld.boss_keys[self.player].value,
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
        elif item_data.treasure and self.multiworld.treasure_check[self.player].value:
            if self.multiworld.john[self.player].value:
                classification = ItemClassification.progression
            else:
                classification = ItemClassification.useful
        elif item_data.trap:
            classification = ItemClassification.trap
        else:
            classification = ItemClassification.filler
        item = PizzaTowerItem(name, classification, item_data.code, self.player)
        return item

    def create_regions(self) -> None:
        def create_region(region_name: str, exits=[]):
            ret = Region(region_name, self.player, self.multiworld)
            for loc_name, loc_data in location_table.items():
                if loc_data.region != region_name:
                    continue
                ret.locations.append(PizzaTowerTask(self.player, loc_name, loc_data.id, ret))
            for exit in exits:
                ret.exits.append(Entrance(self.player, exit, ret))
            return ret

        self.multiworld.regions += [create_region(*r) for r in tower_regions]
        Regions.link_tower_structures(self.multiworld, self.player)

    def create_items(self) -> None:
        Items.create_all_items(self.multiworld, self.player)

    def generate_early(self) -> None:
        world = self.multiworld

        if self.multiworld.boss_keys[self.player].value == 0:
            pass
            # world.push_precollected(self.create_item(Names.pepperman + " Boss Key"))
            # world.push_precollected(self.create_item(Names.vigilante + " Boss Key"))
            # world.push_precollected(self.create_item(Names.noise + " Boss Key"))
            # world.push_precollected(self.create_item(Names.fakepep + " Boss Key"))

        if self.multiworld.treasure_check[self.player].value:
            pass

    def generate_basic(self) -> None:
        world = self.multiworld

        world.get_location("Escape " + Names.tower, self.player) \
            .place_locked_item(self.create_item("Victory"))

        if self.multiworld.boss_keys[self.player].value == 0:
            world.get_location("Defeat " + Names.pepperman, self.player) \
                .place_locked_item(self.create_item(Names.pepperman + " Boss Key"))
            world.get_location("Defeat " + Names.vigilante, self.player) \
                .place_locked_item(self.create_item(Names.vigilante + " Boss Key"))
            world.get_location("Defeat " + Names.noise, self.player) \
                .place_locked_item(self.create_item(Names.noise + " Boss Key"))
            world.get_location("Defeat " + Names.fakepep, self.player) \
                .place_locked_item(self.create_item(Names.fakepep + " Boss Key"))

        if not self.multiworld.treasure_check[self.player].value:
            for i in Locations.treasure_table.keys():
                for j in Items.treasure_table.keys():
                    if i == j:
                        world.get_location(i, self.player) \
                            .place_locked_item(self.create_item(j))

    def set_rules(self) -> None:
        set_rules(self.multiworld, self.player)
