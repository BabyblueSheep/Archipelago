from BaseClasses import MultiWorld
from . import Names, Regions
from .Locations import task_table
from ..AutoWorld import LogicMixin
from ..generic.Rules import forbid_item, set_rule


class PizzaTowerLogic(LogicMixin):
    def _pizza_has_toppins(self, amount: int, player: int):
        return self.count_group("toppins", player) >= amount

    def _pizza_has_treasures(self, amount: int, player: int):
        return self.count_group("treasures", player) >= amount


def set_rules(world: MultiWorld, player: int):
    for name, data in task_table.items():
        if data.region in Regions.floor_1_regions:
            continue
        forbid_item(world.get_location(name, player), Names.pepperman + " Boss Key", player)
        if data.region in Regions.floor_2_regions:
            continue
        forbid_item(world.get_location(name, player), Names.vigilante + " Boss Key", player)
        if data.region in Regions.floor_3_regions:
            continue
        forbid_item(world.get_location(name, player), Names.noise + " Boss Key", player)
        if data.region in Regions.floor_4_regions:
            continue
        forbid_item(world.get_location(name, player), Names.fakepep + " Boss Key", player)

    set_rule(world.get_entrance(Names.pepperman + " Stage", player), lambda state: state._pizza_has_toppins(10, player))
    set_rule(world.get_entrance(Names.vigilante + " Stage", player), lambda state: state._pizza_has_toppins(25, player))
    set_rule(world.get_entrance(Names.noise + " Stage", player), lambda state: state._pizza_has_toppins(45, player))
    set_rule(world.get_entrance(Names.fakepep + " Stage", player), lambda state: state._pizza_has_toppins(65, player))
    set_rule(world.get_entrance(Names.pizzaface + " Stage", player), lambda state: state._pizza_has_toppins(86, player))

    if world.boss_keys[player].value == 0 or world.boss_keys[player].value == 2: # i might use this, idk
        pass

    if world.john[player].value:
        set_rule(world.get_entrance(Names.pizzaface + " Stage", player), lambda state: state._pizza_has_treasures(19, player))

    world.completion_condition[player] = lambda state: state.has("Victory", player)
