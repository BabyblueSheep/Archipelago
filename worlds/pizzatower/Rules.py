from BaseClasses import MultiWorld
from . import Names, Regions
from .Locations import task_table
from ..AutoWorld import LogicMixin
from ..generic.Rules import forbid_item


class PizzaTowerLogic(LogicMixin):
    pass


def set_rules(world: MultiWorld, player: int):
    for name, data in task_table.items():
        if data.region in Regions.floor_1_regions: continue
        forbid_item(world.get_location(name, player), Names.pepperman + " Boss Key", player)

    world.completion_condition[player] = lambda state: state.has("Victory", player)
