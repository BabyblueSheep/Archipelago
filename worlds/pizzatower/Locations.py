from BaseClasses import Location
import typing

from .Names import *


class LocationData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str
    treasure: bool = False


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

location_table = {
    **task_table,
    **treasure_table
}
