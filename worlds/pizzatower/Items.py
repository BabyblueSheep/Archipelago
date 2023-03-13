from BaseClasses import Item, ItemClassification, MultiWorld
from .Names import *
import typing


class ItemData(typing.NamedTuple):
    code: typing.Optional[int]
    required: bool
    trap: bool = False


class PizzaTowerItem(Item):
    game: str = "Pizza Tower"


def create_all_items(world: MultiWorld, player: int) -> None:
    exclude = [item for item in world.precollected_items[player]]

    for name, data in important_table.items():
        item = world.create_item(name, player)
        if item not in exclude:
            world.itempool.append(item)


important_table = {
    entrance + " Mushroom Toppin": ItemData(8820001, True),
    entrance + " Cheese Toppin": ItemData(8820002, True),
    entrance + " Tomato Toppin": ItemData(8820003, True),
    entrance + " Sausage Toppin": ItemData(8820004, True),
    entrance + " Pineapple Toppin": ItemData(8820005, True),
    medieval + " Mushroom Toppin": ItemData(8820011, True),
    medieval + " Cheese Toppin": ItemData(8820012, True),
    medieval + " Tomato Toppin": ItemData(8820013, True),
    medieval + " Sausage Toppin": ItemData(8820014, True),
    medieval + " Pineapple Toppin": ItemData(8820015, True),
    ruin + " Mushroom Toppin": ItemData(8820021, True),
    ruin + " Cheese Toppin": ItemData(8820022, True),
    ruin + " Tomato Toppin": ItemData(8820023, True),
    ruin + " Sausage Toppin": ItemData(8820024, True),
    ruin + " Pineapple Toppin": ItemData(8820025, True),
    dungeon + " Mushroom Toppin": ItemData(8820031, True),
    dungeon + " Cheese Toppin": ItemData(8820032, True),
    dungeon + " Tomato Toppin": ItemData(8820033, True),
    dungeon + " Sausage Toppin": ItemData(8820034, True),
    dungeon + " Pineapple Toppin": ItemData(8820035, True),

    badland + " Mushroom Toppin": ItemData(8820101, True),
    badland + " Cheese Toppin": ItemData(8820102, True),
    badland + " Tomato Toppin": ItemData(8820103, True),
    badland + " Sausage Toppin": ItemData(8820104, True),
    badland + " Pineapple Toppin": ItemData(8820105, True),
    graveyard + " Mushroom Toppin": ItemData(8820111, True),
    graveyard + " Cheese Toppin": ItemData(8820112, True),
    graveyard + " Tomato Toppin": ItemData(8820113, True),
    graveyard + " Sausage Toppin": ItemData(8820114, True),
    graveyard + " Pineapple Toppin": ItemData(8820115, True),
    farm + " Mushroom Toppin": ItemData(8820121, True),
    farm + " Cheese Toppin": ItemData(8820122, True),
    farm + " Tomato Toppin": ItemData(8820123, True),
    farm + " Sausage Toppin": ItemData(8820124, True),
    farm + " Pineapple Toppin": ItemData(8820125, True),
    saloon + " Mushroom Toppin": ItemData(8820131, True),
    saloon + " Cheese Toppin": ItemData(8820132, True),
    saloon + " Tomato Toppin": ItemData(8820133, True),
    saloon + " Sausage Toppin": ItemData(8820134, True),
    saloon + " Pineapple Toppin": ItemData(8820135, True),

    plage + " Mushroom Toppin": ItemData(8820201, True),
    plage + " Cheese Toppin": ItemData(8820202, True),
    plage + " Tomato Toppin": ItemData(8820203, True),
    plage + " Sausage Toppin": ItemData(8820204, True),
    plage + " Pineapple Toppin": ItemData(8820205, True),
    forest + " Mushroom Toppin": ItemData(8820211, True),
    forest + " Cheese Toppin": ItemData(8820212, True),
    forest + " Tomato Toppin": ItemData(8820213, True),
    forest + " Sausage Toppin": ItemData(8820214, True),
    forest + " Pineapple Toppin": ItemData(8820215, True),
    space + " Mushroom Toppin": ItemData(8820221, True),
    space + " Cheese Toppin": ItemData(8820222, True),
    space + " Tomato Toppin": ItemData(8820223, True),
    space + " Sausage Toppin": ItemData(8820224, True),
    space + " Pineapple Toppin": ItemData(8820225, True),
    minigolf + " Mushroom Toppin": ItemData(8820231, True),
    minigolf + " Cheese Toppin": ItemData(8820232, True),
    minigolf + " Tomato Toppin": ItemData(8820233, True),
    minigolf + " Sausage Toppin": ItemData(8820234, True),
    minigolf + " Pineapple Toppin": ItemData(8820235, True),

    street + " Mushroom Toppin": ItemData(8820301, True),
    street + " Cheese Toppin": ItemData(8820302, True),
    street + " Tomato Toppin": ItemData(8820303, True),
    street + " Sausage Toppin": ItemData(8820304, True),
    street + " Pineapple Toppin": ItemData(8820305, True),
    industrial + " Mushroom Toppin": ItemData(8820311, True),
    industrial + " Cheese Toppin": ItemData(8820312, True),
    industrial + " Tomato Toppin": ItemData(8820313, True),
    industrial + " Sausage Toppin": ItemData(8820314, True),
    industrial + " Pineapple Toppin": ItemData(8820315, True),
    sewer + " Mushroom Toppin": ItemData(8820321, True),
    sewer + " Cheese Toppin": ItemData(8820322, True),
    sewer + " Tomato Toppin": ItemData(8820323, True),
    sewer + " Sausage Toppin": ItemData(8820324, True),
    sewer + " Pineapple Toppin": ItemData(8820325, True),
    freezer + " Mushroom Toppin": ItemData(8820331, True),
    freezer + " Cheese Toppin": ItemData(8820332, True),
    freezer + " Tomato Toppin": ItemData(8820333, True),
    freezer + " Sausage Toppin": ItemData(8820334, True),
    freezer + " Pineapple Toppin": ItemData(8820335, True),

    chateau + " Mushroom Toppin": ItemData(8820401, True),
    chateau + " Cheese Toppin": ItemData(8820402, True),
    chateau + " Tomato Toppin": ItemData(8820403, True),
    chateau + " Sausage Toppin": ItemData(8820404, True),
    chateau + " Pineapple Toppin": ItemData(8820405, True),
    kidsparty + " Mushroom Toppin": ItemData(8820411, True),
    kidsparty + " Cheese Toppin": ItemData(8820412, True),
    kidsparty + " Tomato Toppin": ItemData(8820413, True),
    kidsparty + " Sausage Toppin": ItemData(8820414, True),
    kidsparty + " Pineapple Toppin": ItemData(8820415, True),
    war + " Mushroom Toppin": ItemData(8820421, True),
    war + " Cheese Toppin": ItemData(8820422, True),
    war + " Tomato Toppin": ItemData(8820423, True),
    war + " Sausage Toppin": ItemData(8820424, True),
    war + " Pineapple Toppin": ItemData(8820425, True),

    pepperman + " Boss Key": ItemData(8820501, True),
    vigilante + " Boss Key": ItemData(8820501, True),
    noise + " Boss Key": ItemData(8820501, True),
    fakepep + " Boss Key": ItemData(8820501, True),

    "Victory": ItemData(8820999, True)
}

junk_table = {
    "1 Dollar": ItemData(8820601, False),
}

trap_table = {
    "Timer Trap": ItemData(8820601, False, True),
    "Stun Trap": ItemData(8820602, False, True),
    "Transformation Trap": ItemData(8820603, False, True)
}

item_table = {
    **important_table,
    **junk_table,
    **trap_table
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
