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
    entrance + " Mushroom Toppin": ItemData(88201111, False, True),
    entrance + " Cheese Toppin": ItemData(88201211, False, True),
    entrance + " Tomato Toppin": ItemData(88201311, False, True),
    entrance + " Sausage Toppin": ItemData(88201411, False, True),
    entrance + " Pineapple Toppin": ItemData(88201511, False, True),
    medieval + " Mushroom Toppin": ItemData(88201112, False, True),
    medieval + " Cheese Toppin": ItemData(88201212, False, True),
    medieval + " Tomato Toppin": ItemData(88201312, False, True),
    medieval + " Sausage Toppin": ItemData(88201412, False, True),
    medieval + " Pineapple Toppin": ItemData(88201512, False, True),
    ruin + " Mushroom Toppin": ItemData(88201113, False, True),
    ruin + " Cheese Toppin": ItemData(88201213, False, True),
    ruin + " Tomato Toppin": ItemData(88201313, False, True),
    ruin + " Sausage Toppin": ItemData(88201413, False, True),
    ruin + " Pineapple Toppin": ItemData(88201513, False, True),
    dungeon + " Mushroom Toppin": ItemData(88201114, False, True),
    dungeon + " Cheese Toppin": ItemData(88201214, False, True),
    dungeon + " Tomato Toppin": ItemData(88201314, False, True),
    dungeon + " Sausage Toppin": ItemData(88201414, False, True),
    dungeon + " Pineapple Toppin": ItemData(88201514, False, True),

    badland + " Mushroom Toppin": ItemData(88201121, False, True),
    badland + " Cheese Toppin": ItemData(88201221, False, True),
    badland + " Tomato Toppin": ItemData(88201321, False, True),
    badland + " Sausage Toppin": ItemData(88201421, False, True),
    badland + " Pineapple Toppin": ItemData(88201521, False, True),
    graveyard + " Mushroom Toppin": ItemData(88201122, False, True),
    graveyard + " Cheese Toppin": ItemData(88201222, False, True),
    graveyard + " Tomato Toppin": ItemData(88201322, False, True),
    graveyard + " Sausage Toppin": ItemData(88201422, False, True),
    graveyard + " Pineapple Toppin": ItemData(88201522, False, True),
    farm + " Mushroom Toppin": ItemData(88201123, False, True),
    farm + " Cheese Toppin": ItemData(88201223, False, True),
    farm + " Tomato Toppin": ItemData(88201323, False, True),
    farm + " Sausage Toppin": ItemData(88201423, False, True),
    farm + " Pineapple Toppin": ItemData(88201523, False, True),
    saloon + " Mushroom Toppin": ItemData(88201124, False, True),
    saloon + " Cheese Toppin": ItemData(88201224, False, True),
    saloon + " Tomato Toppin": ItemData(88201324, False, True),
    saloon + " Sausage Toppin": ItemData(88201424, False, True),
    saloon + " Pineapple Toppin": ItemData(88201524, False, True),

    plage + " Mushroom Toppin": ItemData(88201131, False, True),
    plage + " Cheese Toppin": ItemData(88201231, False, True),
    plage + " Tomato Toppin": ItemData(88201331, False, True),
    plage + " Sausage Toppin": ItemData(88201431, False, True),
    plage + " Pineapple Toppin": ItemData(88201531, False, True),
    forest + " Mushroom Toppin": ItemData(88201132, False, True),
    forest + " Cheese Toppin": ItemData(88201232, False, True),
    forest + " Tomato Toppin": ItemData(88201332, False, True),
    forest + " Sausage Toppin": ItemData(88201432, False, True),
    forest + " Pineapple Toppin": ItemData(88201532, False, True),
    space + " Mushroom Toppin": ItemData(88201133, False, True),
    space + " Cheese Toppin": ItemData(88201233, False, True),
    space + " Tomato Toppin": ItemData(88201333, False, True),
    space + " Sausage Toppin": ItemData(88201433, False, True),
    space + " Pineapple Toppin": ItemData(88201533, False, True),
    minigolf + " Mushroom Toppin": ItemData(88201134, False, True),
    minigolf + " Cheese Toppin": ItemData(88201234, False, True),
    minigolf + " Tomato Toppin": ItemData(88201334, False, True),
    minigolf + " Sausage Toppin": ItemData(88201434, False, True),
    minigolf + " Pineapple Toppin": ItemData(88201534, False, True),

    street + " Mushroom Toppin": ItemData(88201141, False, True),
    street + " Cheese Toppin": ItemData(88201241, False, True),
    street + " Tomato Toppin": ItemData(88201341, False, True),
    street + " Sausage Toppin": ItemData(88201441, False, True),
    street + " Pineapple Toppin": ItemData(88201541, False, True),
    industrial + " Mushroom Toppin": ItemData(88201142, False, True),
    industrial + " Cheese Toppin": ItemData(88201242, False, True),
    industrial + " Tomato Toppin": ItemData(88201342, False, True),
    industrial + " Sausage Toppin": ItemData(88201442, False, True),
    industrial + " Pineapple Toppin": ItemData(88201542, False, True),
    sewer + " Mushroom Toppin": ItemData(88201143, False, True),
    sewer + " Cheese Toppin": ItemData(88201243, False, True),
    sewer + " Tomato Toppin": ItemData(88201343, False, True),
    sewer + " Sausage Toppin": ItemData(88201443, False, True),
    sewer + " Pineapple Toppin": ItemData(88201543, False, True),
    freezer + " Mushroom Toppin": ItemData(88201144, False, True),
    freezer + " Cheese Toppin": ItemData(88201244, False, True),
    freezer + " Tomato Toppin": ItemData(88201344, False, True),
    freezer + " Sausage Toppin": ItemData(88201444, False, True),
    freezer + " Pineapple Toppin": ItemData(88201544, False, True),

    chateau + " Mushroom Toppin": ItemData(88201151, False, True),
    chateau + " Cheese Toppin": ItemData(88201251, False, True),
    chateau + " Tomato Toppin": ItemData(88201351, False, True),
    chateau + " Sausage Toppin": ItemData(88201451, False, True),
    chateau + " Pineapple Toppin": ItemData(88201551, False, True),
    kidsparty + " Mushroom Toppin": ItemData(88201152, False, True),
    kidsparty + " Cheese Toppin": ItemData(88201252, False, True),
    kidsparty + " Tomato Toppin": ItemData(88201352, False, True),
    kidsparty + " Sausage Toppin": ItemData(88201452, False, True),
    kidsparty + " Pineapple Toppin": ItemData(88201552, False, True),
    war + " Mushroom Toppin": ItemData(88201153, False, True),
    war + " Cheese Toppin": ItemData(88201253, False, True),
    war + " Tomato Toppin": ItemData(88201353, False, True),
    war + " Sausage Toppin": ItemData(88201453, False, True),
    war + " Pineapple Toppin": ItemData(88201553, False, True),
}

important_table = {
    pepperman + " Boss Key": ItemData(88200015, True),
    vigilante + " Boss Key": ItemData(88200025, True),
    noise + " Boss Key": ItemData(88200035, True),
    fakepep + " Boss Key": ItemData(88200045, True),

    "Victory": ItemData(88209999, True)
}

junk_table = {
    "Super Taunt Charge": ItemData(88209000, False, False),
}

trap_table = {
    "Timer Trap": ItemData(88209101, False, False, True),
    "Stun Trap": ItemData(88209102, False, False, True),
    "Transformation Trap": ItemData(88209103, False, False, True)
}

item_table = {
    **toppin_table,
    **important_table,
    **junk_table,
    **trap_table
}

lookup_id_to_name: typing.Dict[int, str] = {data.code: item_name for item_name, data in item_table.items() if data.code}
