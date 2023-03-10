from BaseClasses import MultiWorld
from ..AutoWorld import LogicMixin


class PizzaTowerLogic(LogicMixin):
    pass


def set_rules(world: MultiWorld, player: int):
    world.completion_condition[player] = lambda state: state.has("Victory", player)
