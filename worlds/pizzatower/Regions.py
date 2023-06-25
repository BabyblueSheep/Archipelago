from BaseClasses import MultiWorld, Region, Entrance
from .Names import *
from .Locations import location_table, LocationData, PizzaTowerLocation


def create_region(world: MultiWorld, player: int, name: str, exits=None):
    region = Region(name, player, world)
    loc_name: str
    location: LocationData
    for loc_name in location_table:
        if location_table[loc_name].region == name:
            if (not location_table[loc_name].treasure) or world.treasure_check[player].value:
                region.locations.append(PizzaTowerLocation(player, loc_name, location_table[loc_name].id, region))

    if exits:
        for _exit in exits:
            region.exits.append(Entrance(player, _exit, region))

    return region


def create_regions(world: MultiWorld, player: int):
    if world.shuffle_level[player].value:
        pass
    else:
        for region_name in pizza_tower_regions:
            world.regions.append(create_region(world, player, region_name, pizza_tower_regions[region_name]))
        for region_exit in mandatory_connections:
            world.get_entrance(region_exit, player)\
                .connect(world.get_region(mandatory_connections[region_exit], player))
        for region_exit in default_connections:
            world.get_entrance(region_exit, player)\
                .connect(world.get_region(default_connections[region_exit], player))


pizza_tower_regions = {
    "Menu": {"New File"},
    hub1: {hub1 + " Level 0", hub1 + " Level 1", hub1 + " Level 2", hub1 + " Level 3", hub1 + " Level 4",
           hub1 + " Boss", hub1 + " Exit"},
    hub2: {hub2 + " Level 1", hub2 + " Level 2", hub2 + " Level 3", hub2 + " Level 4",
           hub2 + " Boss", hub2 + " Exit"},
    hub3: {hub3 + " Level 1", hub3 + " Level 2", hub3 + " Level 3", hub3 + " Level 4",
           hub3 + " Boss", hub3 + " Exit"},
    hub4: {hub4 + " Level 1", hub4 + " Level 2", hub4 + " Level 3", hub4 + " Level 4",
           hub4 + " Boss", hub4 + " Exit"},
    hub5: {hub5 + " Level 1", hub5 + " Level 2", hub5 + " Level 3", hub5 + " Level 4",
           hub5 + " Boss"},

    tutorial: {},
    entrance: {},
    medieval: {},
    ruin: {},
    dungeon: {},
    pepperman: {},

    badland: {},
    graveyard: {},
    farm: {},
    saloon: {},
    vigilante: {},

    plage: {},
    forest: {},
    space: {},
    minigolf: {},
    noise: {},

    street: {},
    industrial: {},
    sewer: {},
    freezer: {},
    fakepep: {},

    chateau: {},
    kidsparty: {},
    war: {},
    pizzaface: {"Pizzaface Shower Hall"},
    tower: {}
}

mandatory_connections = {
    "New File": hub1,
    hub1 + " Level 0": tutorial,
    hub1 + " Boss": pepperman,
    hub1 + " Exit": hub2,

    hub2 + " Boss": vigilante,
    hub2 + " Exit": hub3,

    hub3 + " Boss": noise,
    hub3 + " Exit": hub4,

    hub4 + " Boss": fakepep,
    hub4 + " Exit": hub5,

    hub5 + " Boss": pizzaface,
    "Pizzaface Shower Hall": tower,
    hub5 + " Level 4": tower,
}

default_connections = {
    hub1 + " Level 1": entrance,
    hub1 + " Level 2": medieval,
    hub1 + " Level 3": ruin,
    hub1 + " Level 4": dungeon,

    hub2 + " Level 1": badland,
    hub2 + " Level 2": graveyard,
    hub2 + " Level 3": farm,
    hub2 + " Level 4": saloon,

    hub3 + " Level 1": plage,
    hub3 + " Level 2": forest,
    hub3 + " Level 3": space,
    hub3 + " Level 4": minigolf,

    hub4 + " Level 1": street,
    hub4 + " Level 2": industrial,
    hub4 + " Level 3": sewer,
    hub4 + " Level 4": freezer,

    hub5 + " Level 1": chateau,
    hub5 + " Level 2": kidsparty,
    hub5 + " Level 3": war,
}
