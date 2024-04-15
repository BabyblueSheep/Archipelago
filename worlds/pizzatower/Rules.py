from BaseClasses import MultiWorld
from ..generic.Rules import add_rule
from .Names import *
from .Options import *


def set_rules(world: MultiWorld, player: int, world_options: PizzaTowerOptions):
    world.completion_condition[player] = lambda state: \
        state.has("Victory", player)

    add_rule(world.get_entrance(hub1 + " Exit", player),
             lambda state: state.has(pepperman + " Boss Key", player))
    add_rule(world.get_entrance(hub2 + " Exit", player),
             lambda state: state.has(vigilante + " Boss Key", player))
    add_rule(world.get_entrance(hub3 + " Exit", player),
             lambda state: state.has(noise + " Boss Key", player))
    add_rule(world.get_entrance(hub4 + " Exit", player),
             lambda state: state.has(fakepep + " Boss Key", player))

    add_rule(world.get_entrance(hub1 + " Boss", player),
             lambda state: state.count_group("toppins", player) >= 10)
    add_rule(world.get_entrance(hub2 + " Boss", player),
             lambda state: state.count_group("toppins", player) >= 10+15)
    add_rule(world.get_entrance(hub3 + " Boss", player),
             lambda state: state.count_group("toppins", player) >= 10+15+20)
    add_rule(world.get_entrance(hub4 + " Boss", player),
             lambda state: state.count_group("toppins", player) >= 10+15+20+20)
    add_rule(world.get_entrance(hub5 + " Boss", player),
             lambda state: state.count_group("toppins", player) >= 10+15+20+20+21),

    add_rule(world.get_entrance(trickytreat + " Entrance", player),
             lambda state: state.count_group("pumpkins", player) >= 20)

    add_rule(world.get_location("Escape " + trickytreat, player),
             lambda state: bool(world_options.pumpkin_hunt.value))
    add_rule(world.get_location("Escape " + secretlevel, player),
             lambda state: bool(world_options.secret_eye_check.value))
