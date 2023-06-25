from BaseClasses import MultiWorld
from ..generic.Rules import set_rule
from .Names import *


def set_rules(world: MultiWorld, player: int):
    world.completion_condition[player] = lambda state: \
        state.has("Victory", player)

    set_rule(world.get_entrance(hub1 + " Exit", player),
             lambda state: state.has(pepperman + " Boss Key", player))
    set_rule(world.get_entrance(hub2 + " Exit", player),
             lambda state: state.has(vigilante + " Boss Key", player))
    set_rule(world.get_entrance(hub3 + " Exit", player),
             lambda state: state.has(noise + " Boss Key", player))
    set_rule(world.get_entrance(hub4 + " Exit", player),
             lambda state: state.has(fakepep + " Boss Key", player))

    set_rule(world.get_entrance(hub1 + " Boss", player),
             lambda state: state.count_group("toppins", player) >= 10)
    set_rule(world.get_entrance(hub2 + " Boss", player),
             lambda state: state.count_group("toppins", player) >= 10+15)
    set_rule(world.get_entrance(hub3 + " Boss", player),
             lambda state: state.count_group("toppins", player) >= 10+15+20)
    set_rule(world.get_entrance(hub4 + " Boss", player),
             lambda state: state.count_group("toppins", player) >= 10+15+20+20)
    set_rule(world.get_entrance(hub5 + " Boss", player),
             lambda state: state.count_group("toppins", player) >= 10+15+20+20+21)

