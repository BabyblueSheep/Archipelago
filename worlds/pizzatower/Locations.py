from BaseClasses import Location
import typing
from dataclasses import dataclass

from .Names import *


class LocationData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str
    treasure: bool = False
    secret: bool = False
    pumpkin: bool = False


class PizzaTowerLocation(Location):
    game: str = "Pizza Tower"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


task_table = {
    entrance + " Mushroom Toppin":    LocationData(88211111, entrance),
    entrance + " Cheese Toppin":      LocationData(88211211, entrance),
    entrance + " Tomato Toppin":      LocationData(88211311, entrance),
    entrance + " Sausage Toppin":     LocationData(88211411, entrance),
    entrance + " Pineapple Toppin":   LocationData(88211511, entrance),
    medieval + " Mushroom Toppin":    LocationData(88211112, medieval),
    medieval + " Cheese Toppin":      LocationData(88211212, medieval),
    medieval + " Tomato Toppin":      LocationData(88211312, medieval),
    medieval + " Sausage Toppin":     LocationData(88211412, medieval),
    medieval + " Pineapple Toppin":   LocationData(88211512, medieval),
    ruin + " Mushroom Toppin":        LocationData(88211113, ruin),
    ruin + " Cheese Toppin":          LocationData(88211213, ruin),
    ruin + " Tomato Toppin":          LocationData(88211313, ruin),
    ruin + " Sausage Toppin":         LocationData(88211413, ruin),
    ruin + " Pineapple Toppin":       LocationData(88211513, ruin),
    dungeon + " Mushroom Toppin":     LocationData(88211114, dungeon),
    dungeon + " Cheese Toppin":       LocationData(88211214, dungeon),
    dungeon + " Tomato Toppin":       LocationData(88211314, dungeon),
    dungeon + " Sausage Toppin":      LocationData(88211414, dungeon),
    dungeon + " Pineapple Toppin":    LocationData(88211514, dungeon),

    badland + " Mushroom Toppin":     LocationData(88211121, badland),
    badland + " Cheese Toppin":       LocationData(88211221, badland),
    badland + " Tomato Toppin":       LocationData(88211321, badland),
    badland + " Sausage Toppin":      LocationData(88211421, badland),
    badland + " Pineapple Toppin":    LocationData(88211521, badland),
    graveyard + " Mushroom Toppin":   LocationData(88211122, graveyard),
    graveyard + " Cheese Toppin":     LocationData(88211222, graveyard),
    graveyard + " Tomato Toppin":     LocationData(88211322, graveyard),
    graveyard + " Sausage Toppin":    LocationData(88211422, graveyard),
    graveyard + " Pineapple Toppin":  LocationData(88211522, graveyard),
    farm + " Mushroom Toppin":        LocationData(88211123, farm),
    farm + " Cheese Toppin":          LocationData(88211223, farm),
    farm + " Tomato Toppin":          LocationData(88211323, farm),
    farm + " Sausage Toppin":         LocationData(88211423, farm),
    farm + " Pineapple Toppin":       LocationData(88211523, farm),
    saloon + " Mushroom Toppin":      LocationData(88211124, saloon),
    saloon + " Cheese Toppin":        LocationData(88211224, saloon),
    saloon + " Tomato Toppin":        LocationData(88211324, saloon),
    saloon + " Sausage Toppin":       LocationData(88211424, saloon),
    saloon + " Pineapple Toppin":     LocationData(88211524, saloon),

    plage + " Mushroom Toppin":       LocationData(88211131, plage),
    plage + " Cheese Toppin":         LocationData(88211231, plage),
    plage + " Tomato Toppin":         LocationData(88211331, plage),
    plage + " Sausage Toppin":        LocationData(88211431, plage),
    plage + " Pineapple Toppin":      LocationData(88211531, plage),
    forest + " Mushroom Toppin":      LocationData(88211132, forest),
    forest + " Cheese Toppin":        LocationData(88211232, forest),
    forest + " Tomato Toppin":        LocationData(88211332, forest),
    forest + " Sausage Toppin":       LocationData(88211432, forest),
    forest + " Pineapple Toppin":     LocationData(88211532, forest),
    space + " Mushroom Toppin":       LocationData(88211133, space),
    space + " Cheese Toppin":         LocationData(88211233, space),
    space + " Tomato Toppin":         LocationData(88211333, space),
    space + " Sausage Toppin":        LocationData(88211433, space),
    space + " Pineapple Toppin":      LocationData(88211533, space),
    minigolf + " Mushroom Toppin":    LocationData(88211134, minigolf),
    minigolf + " Cheese Toppin":      LocationData(88211234, minigolf),
    minigolf + " Tomato Toppin":      LocationData(88211334, minigolf),
    minigolf + " Sausage Toppin":     LocationData(88211434, minigolf),
    minigolf + " Pineapple Toppin":   LocationData(88211534, minigolf),

    street + " Mushroom Toppin":      LocationData(88211141, street),
    street + " Cheese Toppin":        LocationData(88211241, street),
    street + " Tomato Toppin":        LocationData(88211341, street),
    street + " Sausage Toppin":       LocationData(88211441, street),
    street + " Pineapple Toppin":     LocationData(88211541, street),
    industrial + " Mushroom Toppin":  LocationData(88211142, industrial),
    industrial + " Cheese Toppin":    LocationData(88211242, industrial),
    industrial + " Tomato Toppin":    LocationData(88211342, industrial),
    industrial + " Sausage Toppin":   LocationData(88211442, industrial),
    industrial + " Pineapple Toppin": LocationData(88211542, industrial),
    sewer + " Mushroom Toppin":       LocationData(88211143, sewer),
    sewer + " Cheese Toppin":         LocationData(88211243, sewer),
    sewer + " Tomato Toppin":         LocationData(88211343, sewer),
    sewer + " Sausage Toppin":        LocationData(88211443, sewer),
    sewer + " Pineapple Toppin":      LocationData(88211543, sewer),
    freezer + " Mushroom Toppin":     LocationData(88211144, freezer),
    freezer + " Cheese Toppin":       LocationData(88211244, freezer),
    freezer + " Tomato Toppin":       LocationData(88211344, freezer),
    freezer + " Sausage Toppin":      LocationData(88211444, freezer),
    freezer + " Pineapple Toppin":    LocationData(88211544, freezer),

    chateau + " Mushroom Toppin":     LocationData(88211151, chateau),
    chateau + " Cheese Toppin":       LocationData(88211251, chateau),
    chateau + " Tomato Toppin":       LocationData(88211351, chateau),
    chateau + " Sausage Toppin":      LocationData(88211451, chateau),
    chateau + " Pineapple Toppin":    LocationData(88211551, chateau),
    kidsparty + " Mushroom Toppin":   LocationData(88211152, kidsparty),
    kidsparty + " Cheese Toppin":     LocationData(88211252, kidsparty),
    kidsparty + " Tomato Toppin":     LocationData(88211352, kidsparty),
    kidsparty + " Sausage Toppin":    LocationData(88211452, kidsparty),
    kidsparty + " Pineapple Toppin":  LocationData(88211552, kidsparty),
    war + " Mushroom Toppin":         LocationData(88211153, war),
    war + " Cheese Toppin":           LocationData(88211253, war),
    war + " Tomato Toppin":           LocationData(88211353, war),
    war + " Sausage Toppin":          LocationData(88211453, war),
    war + " Pineapple Toppin":        LocationData(88211553, war),

    "Escape " + tutorial:             LocationData(88210010, tutorial),
    "Escape " + entrance:             LocationData(88210011, entrance),
    "Escape " + medieval:             LocationData(88210012, medieval),
    "Escape " + ruin:                 LocationData(88210013, ruin),
    "Escape " + dungeon:              LocationData(88210014, dungeon),
    "Defeat " + pepperman:            LocationData(88210015, pepperman),

    "Escape " + badland:              LocationData(88210021, badland),
    "Escape " + graveyard:            LocationData(88210022, graveyard),
    "Escape " + farm:                 LocationData(88210023, farm),
    "Escape " + saloon:               LocationData(88210024, saloon),
    "Defeat " + vigilante:            LocationData(88210025, vigilante),

    "Escape " + plage:                LocationData(88210031, plage),
    "Escape " + forest:               LocationData(88210032, forest),
    "Escape " + space:                LocationData(88210033, space),
    "Escape " + minigolf:             LocationData(88210034, minigolf),
    "Defeat " + noise:                LocationData(88210035, noise),

    "Escape " + street:               LocationData(88210041, street),
    "Escape " + industrial:           LocationData(88210042, industrial),
    "Escape " + sewer:                LocationData(88210043, sewer),
    "Escape " + freezer:              LocationData(88210044, freezer),
    "Defeat " + fakepep:              LocationData(88210045, fakepep),

    "Escape " + chateau:              LocationData(88210051, chateau),
    "Escape " + kidsparty:            LocationData(88210052, kidsparty),
    "Escape " + war:                  LocationData(88210053, war),
    "Escape " + tower:                LocationData(88210054, tower),

    "Escape " + secretlevel:          LocationData(88210091, secretlevel),
    "Escape " + trickytreat:          LocationData(88210092, trickytreat),
}

treasure_table = {
    entrance + " Secret Treasure":    LocationData(88212011, entrance, True),
    medieval + " Secret Treasure":    LocationData(88212012, medieval, True),
    ruin + " Secret Treasure":        LocationData(88212013, ruin, True),
    dungeon + " Secret Treasure":     LocationData(88212014, dungeon, True),
    badland + " Secret Treasure":     LocationData(88212021, badland, True),
    graveyard + " Secret Treasure":   LocationData(88212022, graveyard, True),
    farm + " Secret Treasure":        LocationData(88212023, farm, True),
    saloon + " Secret Treasure":      LocationData(88212024, saloon, True),
    plage + " Secret Treasure":       LocationData(88212031, plage, True),
    forest + " Secret Treasure":      LocationData(88212032, forest, True),
    space + " Secret Treasure":       LocationData(88212033, space, True),
    minigolf + " Secret Treasure":    LocationData(88212034, minigolf, True),
    street + " Secret Treasure":      LocationData(88212041, street, True),
    industrial + " Secret Treasure":  LocationData(88212042, industrial, True),
    sewer + " Secret Treasure":       LocationData(88212043, sewer, True),
    freezer + " Secret Treasure":     LocationData(88212044, freezer, True),
    chateau + " Secret Treasure":     LocationData(88212051, chateau, True),
    kidsparty + " Secret Treasure":   LocationData(88212052, kidsparty, True),
    war + " Secret Treasure":         LocationData(88212053, war, True),
}

pumpkin_table = {
    entrance + " Pumpkin":          LocationData(88213011, entrance, False, False, True),
    medieval + " Pumpkin":          LocationData(88213012, medieval, False, False, True),
    ruin + " Pumpkin":              LocationData(88213013, ruin, False, False, True),
    dungeon + " Pumpkin":           LocationData(88213014, dungeon, False, False, True),
    badland + " Pumpkin":           LocationData(88213021, badland, False, False, True),
    graveyard + " Pumpkin":         LocationData(88213022, graveyard, False, False, True),
    farm + " Pumpkin":              LocationData(88213023, farm, False, False, True),
    saloon + " Pumpkin":            LocationData(88213024, saloon, False, False, True),
    plage + " Pumpkin":             LocationData(88213031, plage, False, False, True),
    forest + " Pumpkin":            LocationData(88213032, forest, False, False, True),
    space + " Pumpkin":             LocationData(88213033, space, False, False, True),
    minigolf + " Pumpkin":          LocationData(88213034, minigolf, False, False, True),
    street + " Pumpkin":            LocationData(88213041, street, False, False, True),
    industrial + " Pumpkin":        LocationData(88213042, industrial, False, False, True),
    sewer + " Pumpkin":             LocationData(88213043, sewer, False, False, True),
    freezer + " Pumpkin":           LocationData(88213044, freezer, False, False, True),
    chateau + " Pumpkin":           LocationData(88213051, chateau, False, False, True),
    kidsparty + " Pumpkin":         LocationData(88213052, kidsparty, False, False, True),
    war + " Pumpkin":               LocationData(88213053, war, False, False, True),
    tower + " Pumpkin":             LocationData(88213054, tower, False, False, True),
    trickytreat + " Pumpkin 1":     LocationData(88213901, trickytreat, False, False, True),
    trickytreat + " Pumpkin 2":     LocationData(88213902, trickytreat, False, False, True),
    trickytreat + " Pumpkin 3":     LocationData(88213903, trickytreat, False, False, True),
    trickytreat + " Pumpkin 4":     LocationData(88213904, trickytreat, False, False, True),
    trickytreat + " Pumpkin 5":     LocationData(88213905, trickytreat, False, False, True),
    trickytreat + " Pumpkin 6":     LocationData(88213906, trickytreat, False, False, True),
    trickytreat + " Pumpkin 7":     LocationData(88213907, trickytreat, False, False, True),
    trickytreat + " Pumpkin 8":     LocationData(88213908, trickytreat, False, False, True),
    trickytreat + " Pumpkin 9":     LocationData(88213909, trickytreat, False, False, True),
    trickytreat + " Pumpkin 10":    LocationData(88213910, trickytreat, False, False, True),
}

secret_table = {
    entrance + " Secret Eye 1":     LocationData(88214111, entrance, False, True),
    entrance + " Secret Eye 2":     LocationData(88214112, entrance, False, True),
    entrance + " Secret Eye 3":     LocationData(88214113, entrance, False, True),
    medieval + " Secret Eye 1":     LocationData(88214121, medieval, False, True),
    medieval + " Secret Eye 2":     LocationData(88214122, medieval, False, True),
    medieval + " Secret Eye 3":     LocationData(88214123, medieval, False, True),
    ruin + " Secret Eye 1":         LocationData(88214131, ruin, False, True),
    ruin + " Secret Eye 2":         LocationData(88214132, ruin, False, True),
    ruin + " Secret Eye 3":         LocationData(88214133, ruin, False, True),
    dungeon + " Secret Eye 1":      LocationData(88214141, dungeon, False, True),
    dungeon + " Secret Eye 2":      LocationData(88214142, dungeon, False, True),
    dungeon + " Secret Eye 3":      LocationData(88214143, dungeon, False, True),
    badland + " Secret Eye 1":      LocationData(88214211, badland, False, True),
    badland + " Secret Eye 2":      LocationData(88214212, badland, False, True),
    badland + " Secret Eye 3":      LocationData(88214213, badland, False, True),
    graveyard + " Secret Eye 1":    LocationData(88214221, graveyard, False, True),
    graveyard + " Secret Eye 2":    LocationData(88214222, graveyard, False, True),
    graveyard + " Secret Eye 3":    LocationData(88214223, graveyard, False, True),
    farm + " Secret Eye 1":         LocationData(88214231, farm, False, True),
    farm + " Secret Eye 2":         LocationData(88214232, farm, False, True),
    farm + " Secret Eye 3":         LocationData(88214233, farm, False, True),
    saloon + " Secret Eye 1":       LocationData(88214241, saloon, False, True),
    saloon + " Secret Eye 2":       LocationData(88214242, saloon, False, True),
    saloon + " Secret Eye 3":       LocationData(88214243, saloon, False, True),
    plage + " Secret Eye 1":        LocationData(88214311, plage, False, True),
    plage + " Secret Eye 2":        LocationData(88214312, plage, False, True),
    plage + " Secret Eye 3":        LocationData(88214313, plage, False, True),
    forest + " Secret Eye 1":       LocationData(88214321, forest, False, True),
    forest + " Secret Eye 2":       LocationData(88214322, forest, False, True),
    forest + " Secret Eye 3":       LocationData(88214323, forest, False, True),
    space + " Secret Eye 1":        LocationData(88214331, space, False, True),
    space + " Secret Eye 2":        LocationData(88214332, space, False, True),
    space + " Secret Eye 3":        LocationData(88214333, space, False, True),
    minigolf + " Secret Eye 1":     LocationData(88214341, minigolf, False, True),
    minigolf + " Secret Eye 2":     LocationData(88214342, minigolf, False, True),
    minigolf + " Secret Eye 3":     LocationData(88214343, minigolf, False, True),
    street + " Secret Eye 1":       LocationData(88214411, street, False, True),
    street + " Secret Eye 2":       LocationData(88214412, street, False, True),
    street + " Secret Eye 3":       LocationData(88214413, street, False, True),
    industrial + "Secret Eye 1":   LocationData(88214421, industrial, False, True),
    industrial + "Secret Eye 2":   LocationData(88214422, industrial, False, True),
    industrial + "Secret Eye 3":   LocationData(88214423, industrial, False, True),
    sewer + " Secret Eye 1":        LocationData(88214431, sewer, False, True),
    sewer + " Secret Eye 2":        LocationData(88214432, sewer, False, True),
    sewer + " Secret Eye 3":        LocationData(88214433, sewer, False, True),
    freezer + " Secret Eye 1":      LocationData(88214441, freezer, False, True),
    freezer + " Secret Eye 2":      LocationData(88214442, freezer, False, True),
    freezer + " Secret Eye 3":      LocationData(88214443, freezer, False, True),
    chateau + " Secret Eye 1":      LocationData(88214511, chateau, False, True),
    chateau + " Secret Eye 2":      LocationData(88214512, chateau, False, True),
    chateau + " Secret Eye 3":      LocationData(88214513, chateau, False, True),
    kidsparty + " Secret Eye 1":    LocationData(88214521, kidsparty, False, True),
    kidsparty + " Secret Eye 2":    LocationData(88214522, kidsparty, False, True),
    kidsparty + " Secret Eye 3":    LocationData(88214523, kidsparty, False, True),
    war + "Secret Eye 1":          LocationData(88214531, war, False, True),
    war + "Secret Eye 2":          LocationData(88214532, war, False, True),
    war + "Secret Eye 3":          LocationData(88214533, war, False, True)
}


location_table = {
    **task_table,
    **treasure_table,
    **pumpkin_table,
    **secret_table
}


