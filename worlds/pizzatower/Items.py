from BaseClasses import Item, ItemClassification, MultiWorld
from .Names import *
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    required: bool
    toppin: bool = True
    trap: bool = False


class PizzaTowerItem(Item):
    game: str = "Pizza Tower"


def create_all_items(world: MultiWorld, player: int) -> None:
    exclude = [item for item in world.precollected_items[player]]

    for name, data in important_table.items():
        item = world.create_item(name, player)
        if item not in exclude:
            world.itempool.append(item)

    for name, data in toppin_table.items():
        item = world.create_item(name, player)
        if item not in exclude:
            world.itempool.append(item)


toppin_table = {
    entrance + " Mushroom Toppin": ItemData(8820001, False, True),
    entrance + " Cheese Toppin": ItemData(8820002, False, True),
    entrance + " Tomato Toppin": ItemData(8820003, False, True),
    entrance + " Sausage Toppin": ItemData(8820004, False, True),
    entrance + " Pineapple Toppin": ItemData(8820005, False, True),
    medieval + " Mushroom Toppin": ItemData(8820011, False, True),
    medieval + " Cheese Toppin": ItemData(8820012, False, True),
    medieval + " Tomato Toppin": ItemData(8820013, False, True),
    medieval + " Sausage Toppin": ItemData(8820014, False, True),
    medieval + " Pineapple Toppin": ItemData(8820015, False, True),
    ruin + " Mushroom Toppin": ItemData(8820021, False, True),
    ruin + " Cheese Toppin": ItemData(8820022, False, True),
    ruin + " Tomato Toppin": ItemData(8820023, False, True),
    ruin + " Sausage Toppin": ItemData(8820024, False, True),
    ruin + " Pineapple Toppin": ItemData(8820025, False, True),
    dungeon + " Mushroom Toppin": ItemData(8820031, False, True),
    dungeon + " Cheese Toppin": ItemData(8820032, False, True),
    dungeon + " Tomato Toppin": ItemData(8820033, False, True),
    dungeon + " Sausage Toppin": ItemData(8820034, False, True),
    dungeon + " Pineapple Toppin": ItemData(8820035, False, True),

    badland + " Mushroom Toppin": ItemData(8820101, False, True),
    badland + " Cheese Toppin": ItemData(8820102, False, True),
    badland + " Tomato Toppin": ItemData(8820103, False, True),
    badland + " Sausage Toppin": ItemData(8820104, False, True),
    badland + " Pineapple Toppin": ItemData(8820105, False, True),
    graveyard + " Mushroom Toppin": ItemData(8820111, False, True),
    graveyard + " Cheese Toppin": ItemData(8820112, False, True),
    graveyard + " Tomato Toppin": ItemData(8820113, False, True),
    graveyard + " Sausage Toppin": ItemData(8820114, False, True),
    graveyard + " Pineapple Toppin": ItemData(8820115, False, True),
    farm + " Mushroom Toppin": ItemData(8820121, False, True),
    farm + " Cheese Toppin": ItemData(8820122, False, True),
    farm + " Tomato Toppin": ItemData(8820123, False, True),
    farm + " Sausage Toppin": ItemData(8820124, False, True),
    farm + " Pineapple Toppin": ItemData(8820125, False, True),
    saloon + " Mushroom Toppin": ItemData(8820131, False, True),
    saloon + " Cheese Toppin": ItemData(8820132, False, True),
    saloon + " Tomato Toppin": ItemData(8820133, False, True),
    saloon + " Sausage Toppin": ItemData(8820134, False, True),
    saloon + " Pineapple Toppin": ItemData(8820135, False, True),

    plage + " Mushroom Toppin": ItemData(8820201, False, True),
    plage + " Cheese Toppin": ItemData(8820202, False, True),
    plage + " Tomato Toppin": ItemData(8820203, False, True),
    plage + " Sausage Toppin": ItemData(8820204, False, True),
    plage + " Pineapple Toppin": ItemData(8820205, False, True),
    forest + " Mushroom Toppin": ItemData(8820211, False, True),
    forest + " Cheese Toppin": ItemData(8820212, False, True),
    forest + " Tomato Toppin": ItemData(8820213, False, True),
    forest + " Sausage Toppin": ItemData(8820214, False, True),
    forest + " Pineapple Toppin": ItemData(8820215, False, True),
    space + " Mushroom Toppin": ItemData(8820221, False, True),
    space + " Cheese Toppin": ItemData(8820222, False, True),
    space + " Tomato Toppin": ItemData(8820223, False, True),
    space + " Sausage Toppin": ItemData(8820224, False, True),
    space + " Pineapple Toppin": ItemData(8820225, False, True),
    minigolf + " Mushroom Toppin": ItemData(8820231, False, True),
    minigolf + " Cheese Toppin": ItemData(8820232, False, True),
    minigolf + " Tomato Toppin": ItemData(8820233, False, True),
    minigolf + " Sausage Toppin": ItemData(8820234, False, True),
    minigolf + " Pineapple Toppin": ItemData(8820235, False, True),

    street + " Mushroom Toppin": ItemData(8820301, False, True),
    street + " Cheese Toppin": ItemData(8820302, False, True),
    street + " Tomato Toppin": ItemData(8820303, False, True),
    street + " Sausage Toppin": ItemData(8820304, False, True),
    street + " Pineapple Toppin": ItemData(8820305, False, True),
    industrial + " Mushroom Toppin": ItemData(8820311, False, True),
    industrial + " Cheese Toppin": ItemData(8820312, False, True),
    industrial + " Tomato Toppin": ItemData(8820313, False, True),
    industrial + " Sausage Toppin": ItemData(8820314, False, True),
    industrial + " Pineapple Toppin": ItemData(8820315, False, True),
    sewer + " Mushroom Toppin": ItemData(8820321, False, True),
    sewer + " Cheese Toppin": ItemData(8820322, False, True),
    sewer + " Tomato Toppin": ItemData(8820323, False, True),
    sewer + " Sausage Toppin": ItemData(8820324, False, True),
    sewer + " Pineapple Toppin": ItemData(8820325, False, True),
    freezer + " Mushroom Toppin": ItemData(8820331, False, True),
    freezer + " Cheese Toppin": ItemData(8820332, False, True),
    freezer + " Tomato Toppin": ItemData(8820333, False, True),
    freezer + " Sausage Toppin": ItemData(8820334, False, True),
    freezer + " Pineapple Toppin": ItemData(8820335, False, True),

    chateau + " Mushroom Toppin": ItemData(8820401, False, True),
    chateau + " Cheese Toppin": ItemData(8820402, False, True),
    chateau + " Tomato Toppin": ItemData(8820403, False, True),
    chateau + " Sausage Toppin": ItemData(8820404, False, True),
    chateau + " Pineapple Toppin": ItemData(8820405, False, True),
    kidsparty + " Mushroom Toppin": ItemData(8820411, False, True),
    kidsparty + " Cheese Toppin": ItemData(8820412, False, True),
    kidsparty + " Tomato Toppin": ItemData(8820413, False, True),
    kidsparty + " Sausage Toppin": ItemData(8820414, False, True),
    kidsparty + " Pineapple Toppin": ItemData(8820415, False, True),
    war + " Mushroom Toppin": ItemData(8820421, False, True),
    war + " Cheese Toppin": ItemData(8820422, False, True),
    war + " Tomato Toppin": ItemData(8820423, False, True),
    war + " Sausage Toppin": ItemData(8820424, False, True),
    war + " Pineapple Toppin": ItemData(8820425, False, True),
}

important_table = {
    pepperman + " Boss Key": ItemData(8820501, True),
    vigilante + " Boss Key": ItemData(8820501, True),
    noise + " Boss Key": ItemData(8820501, True),
    fakepep + " Boss Key": ItemData(8820501, True),

    "Victory": ItemData(8820999, True)
}

junk_table = {
    "Super Taunt Charge": ItemData(8820601, False, False),
}

trap_table = {
    "Timer Trap": ItemData(8820601, False, False, True),
    "Stun Trap": ItemData(8820602, False, False, True),
    "Transformation Trap": ItemData(8820603, False, False, True)
}

item_table = {
    **toppin_table,
    **important_table,
    **junk_table,
    **trap_table
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
