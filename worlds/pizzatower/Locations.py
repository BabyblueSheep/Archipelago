from BaseClasses import Location
import typing

from worlds.pizzatower import Names


class LocationData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str
    treasure: bool = False


class PizzaTowerTask(Location):
    game: str = "Pizza Tower"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


task_table = {
    Names.entrance + " Mushroom Toppin": LocationData(88211111, Names.entrance),
    Names.entrance + " Cheese Toppin": LocationData(88211211, Names.entrance),
    Names.entrance + " Tomato Toppin": LocationData(88211311, Names.entrance),
    Names.entrance + " Sausage Toppin": LocationData(88211411, Names.entrance),
    Names.entrance + " Pineapple Toppin": LocationData(88211511, Names.entrance),
    Names.medieval + " Mushroom Toppin": LocationData(88211112, Names.medieval),
    Names.medieval + " Cheese Toppin": LocationData(88211212, Names.medieval),
    Names.medieval + " Tomato Toppin": LocationData(88211312, Names.medieval),
    Names.medieval + " Sausage Toppin": LocationData(88211412, Names.medieval),
    Names.medieval + " Pineapple Toppin": LocationData(88211512, Names.medieval),
    Names.ruin + " Mushroom Toppin": LocationData(88211113, Names.ruin),
    Names.ruin + " Cheese Toppin": LocationData(88211213, Names.ruin),
    Names.ruin + " Tomato Toppin": LocationData(88211313, Names.ruin),
    Names.ruin + " Sausage Toppin": LocationData(88211413, Names.ruin),
    Names.ruin + " Pineapple Toppin": LocationData(88211513, Names.ruin),
    Names.dungeon + " Mushroom Toppin": LocationData(88211114, Names.dungeon),
    Names.dungeon + " Cheese Toppin": LocationData(88211214, Names.dungeon),
    Names.dungeon + " Tomato Toppin": LocationData(88211314, Names.dungeon),
    Names.dungeon + " Sausage Toppin": LocationData(88211414, Names.dungeon),
    Names.dungeon + " Pineapple Toppin": LocationData(88211514, Names.dungeon),

    Names.badland + " Mushroom Toppin": LocationData(88211121, Names.badland),
    Names.badland + " Cheese Toppin": LocationData(88211221, Names.badland),
    Names.badland + " Tomato Toppin": LocationData(88211321, Names.badland),
    Names.badland + " Sausage Toppin": LocationData(88211421, Names.badland),
    Names.badland + " Pineapple Toppin": LocationData(88211521, Names.badland),
    Names.graveyard + " Mushroom Toppin": LocationData(88211122, Names.graveyard),
    Names.graveyard + " Cheese Toppin": LocationData(88211222, Names.graveyard),
    Names.graveyard + " Tomato Toppin": LocationData(88211322, Names.graveyard),
    Names.graveyard + " Sausage Toppin": LocationData(88211422, Names.graveyard),
    Names.graveyard + " Pineapple Toppin": LocationData(88211522, Names.graveyard),
    Names.farm + " Mushroom Toppin": LocationData(88211123, Names.farm),
    Names.farm + " Cheese Toppin": LocationData(88211223, Names.farm),
    Names.farm + " Tomato Toppin": LocationData(88211323, Names.farm),
    Names.farm + " Sausage Toppin": LocationData(88211423, Names.farm),
    Names.farm + " Pineapple Toppin": LocationData(88211523, Names.farm),
    Names.saloon + " Mushroom Toppin": LocationData(88211124, Names.saloon),
    Names.saloon + " Cheese Toppin": LocationData(88211224, Names.saloon),
    Names.saloon + " Tomato Toppin": LocationData(88211324, Names.saloon),
    Names.saloon + " Sausage Toppin": LocationData(88211424, Names.saloon),
    Names.saloon + " Pineapple Toppin": LocationData(88211524, Names.saloon),

    Names.plage + " Mushroom Toppin": LocationData(88211131, Names.plage),
    Names.plage + " Cheese Toppin": LocationData(88211231, Names.plage),
    Names.plage + " Tomato Toppin": LocationData(88211331, Names.plage),
    Names.plage + " Sausage Toppin": LocationData(88211431, Names.plage),
    Names.plage + " Pineapple Toppin": LocationData(88211531, Names.plage),
    Names.forest + " Mushroom Toppin": LocationData(88211132, Names.forest),
    Names.forest + " Cheese Toppin": LocationData(88211232, Names.forest),
    Names.forest + " Tomato Toppin": LocationData(88211332, Names.forest),
    Names.forest + " Sausage Toppin": LocationData(88211432, Names.forest),
    Names.forest + " Pineapple Toppin": LocationData(88211532, Names.forest),
    Names.space + " Mushroom Toppin": LocationData(88211133, Names.space),
    Names.space + " Cheese Toppin": LocationData(88211233, Names.space),
    Names.space + " Tomato Toppin": LocationData(88211333, Names.space),
    Names.space + " Sausage Toppin": LocationData(88211433, Names.space),
    Names.space + " Pineapple Toppin": LocationData(88211533, Names.space),
    Names.minigolf + " Mushroom Toppin": LocationData(88211134, Names.minigolf),
    Names.minigolf + " Cheese Toppin": LocationData(88211234, Names.minigolf),
    Names.minigolf + " Tomato Toppin": LocationData(88211334, Names.minigolf),
    Names.minigolf + " Sausage Toppin": LocationData(88211434, Names.minigolf),
    Names.minigolf + " Pineapple Toppin": LocationData(88211534, Names.minigolf),

    Names.street + " Mushroom Toppin": LocationData(88211141, Names.street),
    Names.street + " Cheese Toppin": LocationData(88211241, Names.street),
    Names.street + " Tomato Toppin": LocationData(88211341, Names.street),
    Names.street + " Sausage Toppin": LocationData(88211441, Names.street),
    Names.street + " Pineapple Toppin": LocationData(88211541, Names.street),
    Names.industrial + " Mushroom Toppin": LocationData(88211142, Names.industrial),
    Names.industrial + " Cheese Toppin": LocationData(88211242, Names.industrial),
    Names.industrial + " Tomato Toppin": LocationData(88211342, Names.industrial),
    Names.industrial + " Sausage Toppin": LocationData(88211442, Names.industrial),
    Names.industrial + " Pineapple Toppin": LocationData(88211542, Names.industrial),
    Names.sewer + " Mushroom Toppin": LocationData(88211143, Names.sewer),
    Names.sewer + " Cheese Toppin": LocationData(88211243, Names.sewer),
    Names.sewer + " Tomato Toppin": LocationData(88211343, Names.sewer),
    Names.sewer + " Sausage Toppin": LocationData(88211443, Names.sewer),
    Names.sewer + " Pineapple Toppin": LocationData(88211543, Names.sewer),
    Names.freezer + " Mushroom Toppin": LocationData(88211144, Names.freezer),
    Names.freezer + " Cheese Toppin": LocationData(88211244, Names.freezer),
    Names.freezer + " Tomato Toppin": LocationData(88211344, Names.freezer),
    Names.freezer + " Sausage Toppin": LocationData(88211444, Names.freezer),
    Names.freezer + " Pineapple Toppin": LocationData(88211544, Names.freezer),

    Names.chateau + " Mushroom Toppin": LocationData(88211151, Names.chateau),
    Names.chateau + " Cheese Toppin": LocationData(88211251, Names.chateau),
    Names.chateau + " Tomato Toppin": LocationData(88211351, Names.chateau),
    Names.chateau + " Sausage Toppin": LocationData(88211451, Names.chateau),
    Names.chateau + " Pineapple Toppin": LocationData(88211551, Names.chateau),
    Names.kidsparty + " Mushroom Toppin": LocationData(88211152, Names.kidsparty),
    Names.kidsparty + " Cheese Toppin": LocationData(88211252, Names.kidsparty),
    Names.kidsparty + " Tomato Toppin": LocationData(88211352, Names.kidsparty),
    Names.kidsparty + " Sausage Toppin": LocationData(88211452, Names.kidsparty),
    Names.kidsparty + " Pineapple Toppin": LocationData(88211552, Names.kidsparty),
    Names.war + " Mushroom Toppin": LocationData(88211153, Names.war),
    Names.war + " Cheese Toppin": LocationData(88211253, Names.war),
    Names.war + " Tomato Toppin": LocationData(88211353, Names.war),
    Names.war + " Sausage Toppin": LocationData(88211453, Names.war),
    Names.war + " Pineapple Toppin": LocationData(88211553, Names.war),

    "Escape " + Names.tutorial: LocationData(88210010, Names.tutorial),
    "Escape " + Names.entrance: LocationData(88210011, Names.entrance),
    "Escape " + Names.medieval: LocationData(88210012, Names.medieval),
    "Escape " + Names.ruin: LocationData(88210013, Names.ruin),
    "Escape " + Names.dungeon: LocationData(88210014, Names.dungeon),
    "Defeat " + Names.pepperman: LocationData(88210015, "Tower Lobby"),

    "Escape " + Names.badland: LocationData(88210021, Names.badland),
    "Escape " + Names.graveyard: LocationData(88210022, Names.graveyard),
    "Escape " + Names.farm: LocationData(88210023, Names.farm),
    "Escape " + Names.saloon: LocationData(88210024, Names.saloon),
    "Defeat " + Names.vigilante: LocationData(88210025, "Western District"),

    "Escape " + Names.plage: LocationData(88210031, Names.plage),
    "Escape " + Names.forest: LocationData(88210032, Names.forest),
    "Escape " + Names.space: LocationData(88210033, Names.space),
    "Escape " + Names.minigolf: LocationData(88210034, Names.minigolf),
    "Defeat " + Names.noise: LocationData(88210035, "Vacation Resort"),

    "Escape " + Names.street: LocationData(88210041, Names.street),
    "Escape " + Names.industrial: LocationData(88210042, Names.industrial),
    "Escape " + Names.sewer: LocationData(88210043, Names.sewer),
    "Escape " + Names.freezer: LocationData(88210044, Names.freezer),
    "Defeat " + Names.fakepep: LocationData(88210045, "Slum"),

    "Escape " + Names.chateau: LocationData(88210051, Names.chateau),
    "Escape " + Names.kidsparty: LocationData(88210052, Names.kidsparty),
    "Escape " + Names.war: LocationData(88210053, Names.war),
    "Escape " + Names.tower: LocationData(88210054, Names.tower),
}

treasure_table = {
    Names.entrance + " Secret Treasure": LocationData(88212011, Names.entrance, True),
    Names.medieval + " Secret Treasure": LocationData(88212012, Names.medieval, True),
    Names.ruin + " Secret Treasure": LocationData(88212013, Names.ruin, True),
    Names.dungeon + " Secret Treasure": LocationData(88212014, Names.dungeon, True),
    Names.badland + " Secret Treasure": LocationData(88212021, Names.badland, True),
    Names.graveyard + " Secret Treasure": LocationData(88212022, Names.graveyard, True),
    Names.farm + " Secret Treasure": LocationData(88212023, Names.farm, True),
    Names.saloon + " Secret Treasure": LocationData(88212024, Names.saloon, True),
    Names.plage + " Secret Treasure": LocationData(88212031, Names.plage, True),
    Names.forest + " Secret Treasure": LocationData(88212032, Names.forest, True),
    Names.space + " Secret Treasure": LocationData(88212033, Names.space, True),
    Names.minigolf + " Secret Treasure": LocationData(88212034, Names.minigolf, True),
    Names.street + " Secret Treasure": LocationData(88212041, Names.street, True),
    Names.industrial + " Secret Treasure": LocationData(88212042, Names.industrial, True),
    Names.sewer + " Secret Treasure": LocationData(88212043, Names.sewer, True),
    Names.freezer + " Secret Treasure": LocationData(88212044, Names.freezer, True),
    Names.chateau + " Secret Treasure": LocationData(88212051, Names.chateau, True),
    Names.kidsparty + " Secret Treasure": LocationData(88212052, Names.kidsparty, True),
    Names.war + " Secret Treasure": LocationData(88212053, Names.war),
}

location_table = {
    **task_table,
    **treasure_table
}

exclusion_table = {

}
