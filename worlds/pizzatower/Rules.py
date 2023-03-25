from BaseClasses import MultiWorld
from . import Names, Regions
from .Locations import task_table
from ..AutoWorld import LogicMixin
from ..generic.Rules import forbid_item, set_rule


class PizzaTowerLogic(LogicMixin):
    def _pizza_has_toppins(self, player: int, amount: int):
        return self.count_group("toppins", player) >= amount


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

    set_rule(world.get_entrance(Names.pepperman + " Stage", player), lambda state: state._pizza_has_toppins(player, 10))
    set_rule(world.get_entrance(Names.vigilante + " Stage", player), lambda state: state._pizza_has_toppins(player, 25))
    set_rule(world.get_entrance(Names.noise + " Stage", player), lambda state: state._pizza_has_toppins(player, 45))
    set_rule(world.get_entrance(Names.fakepep + " Stage", player), lambda state: state._pizza_has_toppins(player, 65))
    set_rule(world.get_entrance(Names.pizzaface + " Stage", player), lambda state: state._pizza_has_toppins(player, 86))

    if world.boss_keys[player].value == 0 or world.boss_keys[player].value == 2: # i might use this, idk
        pass

    world.completion_condition[player] = lambda state: state.has("Victory", player)
