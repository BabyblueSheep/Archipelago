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
    "Escape " + Names.tutorial: LocationData(8821000, Names.tutorial),
    "Escape " + Names.entrance: LocationData(8821001, Names.entrance),
    "Escape " + Names.medieval: LocationData(8821002, Names.medieval),
    "Escape " + Names.ruin: LocationData(8821003, Names.ruin),
    "Escape " + Names.dungeon: LocationData(8821004, Names.dungeon),
    "Defeat " + Names.pepperman: LocationData(8821005, "Tower Lobby"),
    "Escape " + Names.badland: LocationData(8821011, Names.badland),
    "Escape " + Names.graveyard: LocationData(8821012, Names.graveyard),
    "Escape " + Names.farm: LocationData(8821013, Names.farm),
    "Escape " + Names.saloon: LocationData(8821014, Names.saloon),
    "Defeat " + Names.vigilante: LocationData(8821015, "Western District"),
    "Escape " + Names.plage: LocationData(8821021, Names.plage),
    "Escape " + Names.forest: LocationData(8821022, Names.forest),
    "Escape " + Names.space: LocationData(8821023, Names.space),
    "Escape " + Names.minigolf: LocationData(8821024, Names.minigolf),
    "Defeat " + Names.noise: LocationData(8821025, "Vacation Resort"),
    "Escape " + Names.street: LocationData(8821031, Names.street),
    "Escape " + Names.industrial: LocationData(8821032, Names.industrial),
    "Escape " + Names.sewer: LocationData(8821033, Names.sewer),
    "Escape " + Names.freezer: LocationData(8821034, Names.freezer),
    "Defeat " + Names.fakepep: LocationData(8821035, "Slum"),
    "Escape " + Names.chateau: LocationData(8821041, Names.chateau),
    "Escape " + Names.kidsparty: LocationData(8821042, Names.kidsparty),
    "Escape " + Names.war: LocationData(8821043, Names.war),
    "Defeat " + Names.pizzaface: LocationData(8821045, "Staff Only"),
    "Escape " + Names.tower: LocationData(8821044, Names.tower)
}

secret_treasure_table = {
    Names.entrance + " Secret Treasure": LocationData(8821051, Names.entrance),
    Names.medieval + " Secret Treasure": LocationData(8821052, Names.medieval),
    Names.ruin + " Secret Treasure": LocationData(8821053, Names.ruin),
    Names.dungeon + " Secret Treasure": LocationData(8821054, Names.dungeon),
    Names.badland + " Secret Treasure": LocationData(8821061, Names.badland),
    Names.graveyard + " Secret Treasure": LocationData(8821062, Names.graveyard),
    Names.farm + " Secret Treasure": LocationData(8821063, Names.farm),
    Names.saloon + " Secret Treasure": LocationData(8821064, Names.saloon),
    Names.plage + " Secret Treasure": LocationData(8821071, Names.plage),
    Names.forest + " Secret Treasure": LocationData(8821072, Names.forest),
    Names.space + " Secret Treasure": LocationData(8821073, Names.space),
    Names.minigolf + " Secret Treasure": LocationData(8821074, Names.minigolf),
    Names.street + " Secret Treasure": LocationData(8821081, Names.street),
    Names.industrial + " Secret Treasure": LocationData(8821082, Names.industrial),
    Names.sewer + " Secret Treasure": LocationData(8821083, Names.sewer),
    Names.freezer + " Secret Treasure": LocationData(8821084, Names.freezer),
    Names.chateau + " Secret Treasure": LocationData(8821091, Names.chateau),
    Names.kidsparty + " Secret Treasure": LocationData(8821092, Names.kidsparty),
    Names.war + " Secret Treasure": LocationData(8821093, Names.war),
}

exclusion_table = {

}
