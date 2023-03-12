from BaseClasses import Location
import typing

from worlds.pizzatower import Names


class LocationData(typing.NamedTuple):
    id: typing.Optional[int]
    region: str


class PizzaTowerTask(Location):
    game: str = "Pizza Tower"

    def __init__(self, player: int, name: str, address: typing.Optional[int], parent):
        super().__init__(player, name, address, parent)
        self.event = not address


task_table = {
    Names.entrance + " Mushroom Toppin": LocationData(8821001, Names.entrance),
    Names.entrance + " Cheese Toppin": LocationData(8821002, Names.entrance),
    Names.entrance + " Tomato Toppin": LocationData(8821003, Names.entrance),
    Names.entrance + " Sausage Toppin": LocationData(8821004, Names.entrance),
    Names.entrance + " Pineapple Toppin": LocationData(8821005, Names.entrance),
    Names.medieval + " Mushroom Toppin": LocationData(8821011, Names.medieval),
    Names.medieval + " Cheese Toppin": LocationData(8821012, Names.medieval),
    Names.medieval + " Tomato Toppin": LocationData(8821013, Names.medieval),
    Names.medieval + " Sausage Toppin": LocationData(8821014, Names.medieval),
    Names.medieval + " Pineapple Toppin": LocationData(8821015, Names.medieval),
    Names.ruin + " Mushroom Toppin": LocationData(8821021, Names.ruin),
    Names.ruin + " Cheese Toppin": LocationData(8821022, Names.ruin),
    Names.ruin + " Tomato Toppin": LocationData(8821023, Names.ruin),
    Names.ruin + " Sausage Toppin": LocationData(8821024, Names.ruin),
    Names.ruin + " Pineapple Toppin": LocationData(8821025, Names.ruin),
    Names.dungeon + " Mushroom Toppin": LocationData(8821031, Names.dungeon),
    Names.dungeon + " Cheese Toppin": LocationData(8821032, Names.dungeon),
    Names.dungeon + " Tomato Toppin": LocationData(8821033, Names.dungeon),
    Names.dungeon + " Sausage Toppin": LocationData(8821034, Names.dungeon),
    Names.dungeon + " Pineapple Toppin": LocationData(8821035, Names.dungeon),

    Names.badland + " Mushroom Toppin": LocationData(8821101, Names.badland),
    Names.badland + " Cheese Toppin": LocationData(8821102, Names.badland),
    Names.badland + " Tomato Toppin": LocationData(8821103, Names.badland),
    Names.badland + " Sausage Toppin": LocationData(8821104, Names.badland),
    Names.badland + " Pineapple Toppin": LocationData(8821105, Names.badland),
    Names.graveyard + " Mushroom Toppin": LocationData(8821111, Names.graveyard),
    Names.graveyard + " Cheese Toppin": LocationData(8821112, Names.graveyard),
    Names.graveyard + " Tomato Toppin": LocationData(8821113, Names.graveyard),
    Names.graveyard + " Sausage Toppin": LocationData(8821114, Names.graveyard),
    Names.graveyard + " Pineapple Toppin": LocationData(8821115, Names.graveyard),
    Names.farm + " Mushroom Toppin": LocationData(8821121, Names.farm),
    Names.farm + " Cheese Toppin": LocationData(8821122, Names.farm),
    Names.farm + " Tomato Toppin": LocationData(8821123, Names.farm),
    Names.farm + " Sausage Toppin": LocationData(8821124, Names.farm),
    Names.farm + " Pineapple Toppin": LocationData(8821125, Names.farm),
    Names.saloon + " Mushroom Toppin": LocationData(8821131, Names.saloon),
    Names.saloon + " Cheese Toppin": LocationData(8821132, Names.saloon),
    Names.saloon + " Tomato Toppin": LocationData(8821133, Names.saloon),
    Names.saloon + " Sausage Toppin": LocationData(8821134, Names.saloon),
    Names.saloon + " Pineapple Toppin": LocationData(8821135, Names.saloon),

    Names.plage + " Mushroom Toppin": LocationData(8821201, Names.plage),
    Names.plage + " Cheese Toppin": LocationData(8821202, Names.plage),
    Names.plage + " Tomato Toppin": LocationData(8821203, Names.plage),
    Names.plage + " Sausage Toppin": LocationData(8821204, Names.plage),
    Names.plage + " Pineapple Toppin": LocationData(8821205, Names.plage),
    Names.forest + " Mushroom Toppin": LocationData(8821211, Names.forest),
    Names.forest + " Cheese Toppin": LocationData(8821212, Names.forest),
    Names.forest + " Tomato Toppin": LocationData(8821213, Names.forest),
    Names.forest + " Sausage Toppin": LocationData(8821214, Names.forest),
    Names.forest + " Pineapple Toppin": LocationData(8821215, Names.forest),
    Names.space + " Mushroom Toppin": LocationData(8821221, Names.space),
    Names.space + " Cheese Toppin": LocationData(8821222, Names.space),
    Names.space + " Tomato Toppin": LocationData(8821223, Names.space),
    Names.space + " Sausage Toppin": LocationData(8821224, Names.space),
    Names.space + " Pineapple Toppin": LocationData(8821225, Names.space),
    Names.minigolf + " Mushroom Toppin": LocationData(8821231, Names.minigolf),
    Names.minigolf + " Cheese Toppin": LocationData(8821232, Names.minigolf),
    Names.minigolf + " Tomato Toppin": LocationData(8821233, Names.minigolf),
    Names.minigolf + " Sausage Toppin": LocationData(8821234, Names.minigolf),
    Names.minigolf + " Pineapple Toppin": LocationData(8821235, Names.minigolf),

    Names.street + " Mushroom Toppin": LocationData(8821301, Names.street),
    Names.street + " Cheese Toppin": LocationData(8821302, Names.street),
    Names.street + " Tomato Toppin": LocationData(8821303, Names.street),
    Names.street + " Sausage Toppin": LocationData(8821304, Names.street),
    Names.street + " Pineapple Toppin": LocationData(8821305, Names.street),
    Names.industrial + " Mushroom Toppin": LocationData(8821311, Names.industrial),
    Names.industrial + " Cheese Toppin": LocationData(8821312, Names.industrial),
    Names.industrial + " Tomato Toppin": LocationData(8821313, Names.industrial),
    Names.industrial + " Sausage Toppin": LocationData(8821314, Names.industrial),
    Names.industrial + " Pineapple Toppin": LocationData(8821315, Names.industrial),
    Names.sewer + " Mushroom Toppin": LocationData(8821321, Names.sewer),
    Names.sewer + " Cheese Toppin": LocationData(8821322, Names.sewer),
    Names.sewer + " Tomato Toppin": LocationData(8821323, Names.sewer),
    Names.sewer + " Sausage Toppin": LocationData(8821324, Names.sewer),
    Names.sewer + " Pineapple Toppin": LocationData(8821325, Names.sewer),
    Names.freezer + " Mushroom Toppin": LocationData(8821331, Names.freezer),
    Names.freezer + " Cheese Toppin": LocationData(8821332, Names.freezer),
    Names.freezer + " Tomato Toppin": LocationData(8821333, Names.freezer),
    Names.freezer + " Sausage Toppin": LocationData(8821334, Names.freezer),
    Names.freezer + " Pineapple Toppin": LocationData(8821335, Names.freezer),

    Names.chateau + " Mushroom Toppin": LocationData(8821401, Names.chateau),
    Names.chateau + " Cheese Toppin": LocationData(8821402, Names.chateau),
    Names.chateau + " Tomato Toppin": LocationData(8821403, Names.chateau),
    Names.chateau + " Sausage Toppin": LocationData(8821404, Names.chateau),
    Names.chateau + " Pineapple Toppin": LocationData(8821405, Names.chateau),
    Names.kidsparty + " Mushroom Toppin": LocationData(8821411, Names.kidsparty),
    Names.kidsparty + " Cheese Toppin": LocationData(8821412, Names.kidsparty),
    Names.kidsparty + " Tomato Toppin": LocationData(8821413, Names.kidsparty),
    Names.kidsparty + " Sausage Toppin": LocationData(8821414, Names.kidsparty),
    Names.kidsparty + " Pineapple Toppin": LocationData(8821415, Names.kidsparty),
    Names.war + " Mushroom Toppin": LocationData(8821421, Names.war),
    Names.war + " Cheese Toppin": LocationData(8821422, Names.war),
    Names.war + " Tomato Toppin": LocationData(8821423, Names.war),
    Names.war + " Sausage Toppin": LocationData(8821424, Names.war),
    Names.war + " Pineapple Toppin": LocationData(8821425, Names.war),

    "Escape " + Names.tutorial: LocationData(8821500, Names.tutorial),
    "Escape " + Names.entrance: LocationData(8821501, Names.entrance),
    "Escape " + Names.medieval: LocationData(8821502, Names.medieval),
    "Escape " + Names.ruin: LocationData(8821503, Names.ruin),
    "Escape " + Names.dungeon: LocationData(8821504, Names.dungeon),
    "Defeat " + Names.pepperman: LocationData(8821505, "Tower Lobby"),

    "Escape " + Names.badland: LocationData(8821511, Names.badland),
    "Escape " + Names.graveyard: LocationData(8821512, Names.graveyard),
    "Escape " + Names.farm: LocationData(8821513, Names.farm),
    "Escape " + Names.saloon: LocationData(8821514, Names.saloon),
    "Defeat " + Names.vigilante: LocationData(8821515, "Western District"),

    "Escape " + Names.plage: LocationData(8821521, Names.plage),
    "Escape " + Names.forest: LocationData(8821522, Names.forest),
    "Escape " + Names.space: LocationData(8821523, Names.space),
    "Escape " + Names.minigolf: LocationData(8821524, Names.minigolf),
    "Defeat " + Names.noise: LocationData(8821525, "Vacation Resort"),

    "Escape " + Names.street: LocationData(8821531, Names.street),
    "Escape " + Names.industrial: LocationData(8821532, Names.industrial),
    "Escape " + Names.sewer: LocationData(8821533, Names.sewer),
    "Escape " + Names.freezer: LocationData(8821534, Names.freezer),
    "Defeat " + Names.fakepep: LocationData(8821535, "Slum"),

    "Escape " + Names.chateau: LocationData(8821541, Names.chateau),
    "Escape " + Names.kidsparty: LocationData(8821542, Names.kidsparty),
    "Escape " + Names.war: LocationData(8821543, Names.war),
    "Defeat " + Names.pizzaface: LocationData(8821545, "Staff Only"),
    "Escape " + Names.tower: LocationData(8821544, Names.tower),
}

exclusion_table = {

}
