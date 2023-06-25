import math

from BaseClasses import Item, ItemClassification, MultiWorld
from .Names import *
from typing import Dict, NamedTuple, Optional


class ItemData(NamedTuple):
    code: Optional[int]
    required: bool
    treasure: bool = False
    trap: bool = False


class PizzaTowerItem(Item):
    game: str = "Pizza Tower"


def create_item(world: MultiWorld, name: str, player: int) -> PizzaTowerItem:
    item_data = item_table[name]
    if item_data.required:
        classification = ItemClassification.progression
    elif item_data.treasure and world.treasure_check[player].value:
        if world.john[player].value:
            classification = ItemClassification.progression
        else:
            classification = ItemClassification.useful
    elif item_data.trap:
        classification = ItemClassification.trap
    else:
        classification = ItemClassification.filler
    item = PizzaTowerItem(name, classification, item_data.code, player)
    return item


def create_all_items(world: MultiWorld, player: int) -> None:
    exclude = [item for item in world.precollected_items[player]]
    exclude.append(world.create_item("Victory", player))

    if world.boss_keys[player].value == 0:
        exclude.append(world.create_item(pepperman + " Boss Key", player))
        exclude.append(world.create_item(vigilante + " Boss Key", player))
        exclude.append(world.create_item(noise + " Boss Key", player))
        exclude.append(world.create_item(fakepep + " Boss Key", player))

    for name, data in important_table.items():
        item = world.create_item(name, player)
        if item not in exclude:
            world.itempool.append(item)

    for name, data in toppin_table.items():
        item = world.create_item(name, player)
        if item not in exclude:
            world.itempool.append(item)

    for name, data in treasure_table.items():
        item = world.create_item(name, player)
        if world.treasure_check[player].value:
            if item not in exclude:
                world.itempool.append(item)

    junk_count = 20
    trap_weights = []
    trap_weights += (["Stun Trap"] * world.timer_trap[player].value)
    trap_weights += (["Timer Trap"] * world.stun_trap[player].value)
    trap_weights += (["Transformation Trap"] * world.transformation_trap[player].value)
    trap_count = 0 if (len(trap_weights) == 0) else math.ceil(
        junk_count * (world.trap_fill_percentage[player].value / 100.0))
    junk_count -= trap_count

    trap_pool = []
    for i in range(trap_count):
        item = world.create_item(world.random.choice(trap_weights), player)
        trap_pool.append(item)

    world.itempool += trap_pool
    world.itempool += [world.create_item("Super Taunt Charge", player) for _ in range(junk_count)]


toppin_table = {
    entrance + " Mushroom Toppin":      ItemData(88201111, True),
    entrance + " Cheese Toppin":        ItemData(88201211, True),
    entrance + " Tomato Toppin":        ItemData(88201311, True),
    entrance + " Sausage Toppin":       ItemData(88201411, True),
    entrance + " Pineapple Toppin":     ItemData(88201511, True),
    medieval + " Mushroom Toppin":      ItemData(88201112, True),
    medieval + " Cheese Toppin":        ItemData(88201212, True),
    medieval + " Tomato Toppin":        ItemData(88201312, True),
    medieval + " Sausage Toppin":       ItemData(88201412, True),
    medieval + " Pineapple Toppin":     ItemData(88201512, True),
    ruin + " Mushroom Toppin":          ItemData(88201113, True),
    ruin + " Cheese Toppin":            ItemData(88201213, True),
    ruin + " Tomato Toppin":            ItemData(88201313, True),
    ruin + " Sausage Toppin":           ItemData(88201413, True),
    ruin + " Pineapple Toppin":         ItemData(88201513, True),
    dungeon + " Mushroom Toppin":       ItemData(88201114, True),
    dungeon + " Cheese Toppin":         ItemData(88201214, True),
    dungeon + " Tomato Toppin":         ItemData(88201314, True),
    dungeon + " Sausage Toppin":        ItemData(88201414, True),
    dungeon + " Pineapple Toppin":      ItemData(88201514, True),

    badland + " Mushroom Toppin":       ItemData(88201121, True),
    badland + " Cheese Toppin":         ItemData(88201221, True),
    badland + " Tomato Toppin":         ItemData(88201321, True),
    badland + " Sausage Toppin":        ItemData(88201421, True),
    badland + " Pineapple Toppin":      ItemData(88201521, True),
    graveyard + " Mushroom Toppin":     ItemData(88201122, True),
    graveyard + " Cheese Toppin":       ItemData(88201222, True),
    graveyard + " Tomato Toppin":       ItemData(88201322, True),
    graveyard + " Sausage Toppin":      ItemData(88201422, True),
    graveyard + " Pineapple Toppin":    ItemData(88201522, True),
    farm + " Mushroom Toppin":          ItemData(88201123, True),
    farm + " Cheese Toppin":            ItemData(88201223, True),
    farm + " Tomato Toppin":            ItemData(88201323, True),
    farm + " Sausage Toppin":           ItemData(88201423, True),
    farm + " Pineapple Toppin":         ItemData(88201523, True),
    saloon + " Mushroom Toppin":        ItemData(88201124, True),
    saloon + " Cheese Toppin":          ItemData(88201224, True),
    saloon + " Tomato Toppin":          ItemData(88201324, True),
    saloon + " Sausage Toppin":         ItemData(88201424, True),
    saloon + " Pineapple Toppin":       ItemData(88201524, True),

    plage + " Mushroom Toppin":         ItemData(88201131, True),
    plage + " Cheese Toppin":           ItemData(88201231, True),
    plage + " Tomato Toppin":           ItemData(88201331, True),
    plage + " Sausage Toppin":          ItemData(88201431, True),
    plage + " Pineapple Toppin":        ItemData(88201531, True),
    forest + " Mushroom Toppin":        ItemData(88201132, True),
    forest + " Cheese Toppin":          ItemData(88201232, True),
    forest + " Tomato Toppin":          ItemData(88201332, True),
    forest + " Sausage Toppin":         ItemData(88201432, True),
    forest + " Pineapple Toppin":       ItemData(88201532, True),
    space + " Mushroom Toppin":         ItemData(88201133, True),
    space + " Cheese Toppin":           ItemData(88201233, True),
    space + " Tomato Toppin":           ItemData(88201333, True),
    space + " Sausage Toppin":          ItemData(88201433, True),
    space + " Pineapple Toppin":        ItemData(88201533, True),
    minigolf + " Mushroom Toppin":      ItemData(88201134, True),
    minigolf + " Cheese Toppin":        ItemData(88201234, True),
    minigolf + " Tomato Toppin":        ItemData(88201334, True),
    minigolf + " Sausage Toppin":       ItemData(88201434, True),
    minigolf + " Pineapple Toppin":     ItemData(88201534, True),

    street + " Mushroom Toppin":        ItemData(88201141, True),
    street + " Cheese Toppin":          ItemData(88201241, True),
    street + " Tomato Toppin":          ItemData(88201341, True),
    street + " Sausage Toppin":         ItemData(88201441, True),
    street + " Pineapple Toppin":       ItemData(88201541, True),
    industrial + " Mushroom Toppin":    ItemData(88201142, True),
    industrial + " Cheese Toppin":      ItemData(88201242, True),
    industrial + " Tomato Toppin":      ItemData(88201342, True),
    industrial + " Sausage Toppin":     ItemData(88201442, True),
    industrial + " Pineapple Toppin":   ItemData(88201542, True),
    sewer + " Mushroom Toppin":         ItemData(88201143, True),
    sewer + " Cheese Toppin":           ItemData(88201243, True),
    sewer + " Tomato Toppin":           ItemData(88201343, True),
    sewer + " Sausage Toppin":          ItemData(88201443, True),
    sewer + " Pineapple Toppin":        ItemData(88201543, True),
    freezer + " Mushroom Toppin":       ItemData(88201144, True),
    freezer + " Cheese Toppin":         ItemData(88201244, True),
    freezer + " Tomato Toppin":         ItemData(88201344, True),
    freezer + " Sausage Toppin":        ItemData(88201444, True),
    freezer + " Pineapple Toppin":      ItemData(88201544, True),

    chateau + " Mushroom Toppin":       ItemData(88201151, True),
    chateau + " Cheese Toppin":         ItemData(88201251, True),
    chateau + " Tomato Toppin":         ItemData(88201351, True),
    chateau + " Sausage Toppin":        ItemData(88201451, True),
    chateau + " Pineapple Toppin":      ItemData(88201551, True),
    kidsparty + " Mushroom Toppin":     ItemData(88201152, True),
    kidsparty + " Cheese Toppin":       ItemData(88201252, True),
    kidsparty + " Tomato Toppin":       ItemData(88201352, True),
    kidsparty + " Sausage Toppin":      ItemData(88201452, True),
    kidsparty + " Pineapple Toppin":    ItemData(88201552, True),
    war + " Mushroom Toppin":           ItemData(88201153, True),
    war + " Cheese Toppin":             ItemData(88201253, True),
    war + " Tomato Toppin":             ItemData(88201353, True),
    war + " Sausage Toppin":            ItemData(88201453, True),
    war + " Pineapple Toppin":          ItemData(88201553, True),
}

important_table = {
    pepperman + " Boss Key":            ItemData(88200015, True),
    vigilante + " Boss Key":            ItemData(88200025, True),
    noise + " Boss Key":                ItemData(88200035, True),
    fakepep + " Boss Key":              ItemData(88200045, True),

    "Victory":                          ItemData(88209999, True)
}

treasure_table = {
    entrance + " Secret Treasure":      ItemData(88202011, False, True),
    medieval + " Secret Treasure":      ItemData(88202012, False, True),
    ruin + " Secret Treasure":          ItemData(88202013, False, True),
    dungeon + " Secret Treasure":       ItemData(88202014, False, True),
    badland + " Secret Treasure":       ItemData(88202021, False, True),
    graveyard + " Secret Treasure":     ItemData(88202022, False, True),
    farm + " Secret Treasure":          ItemData(88202023, False, True),
    saloon + " Secret Treasure":        ItemData(88202024, False, True),
    plage + " Secret Treasure":         ItemData(88202031, False, True),
    forest + " Secret Treasure":        ItemData(88202032, False, True),
    space + " Secret Treasure":         ItemData(88202033, False, True),
    minigolf + " Secret Treasure":      ItemData(88202034, False, True),
    street + " Secret Treasure":        ItemData(88202041, False, True),
    industrial + " Secret Treasure":    ItemData(88202042, False, True),
    sewer + " Secret Treasure":         ItemData(88202043, False, True),
    freezer + " Secret Treasure":       ItemData(88202044, False, True),
    chateau + " Secret Treasure":       ItemData(88202051, False, True),
    kidsparty + " Secret Treasure":     ItemData(88202052, False, True),
    war + " Secret Treasure":           ItemData(88202053, False, True),
}

junk_table = {
    "Super Taunt Charge":               ItemData(88209000, False),
}

trap_table = {
    "Timer Trap":                       ItemData(88209101, False, False, True),
    "Stun Trap":                        ItemData(88209102, False, False, True),
    "Transformation Trap":              ItemData(88209103, False, False, True)
}

item_table = {
    **toppin_table,
    **important_table,
    **treasure_table,
    **junk_table,
    **trap_table
}