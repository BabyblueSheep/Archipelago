from . import Names


def link_tower_structures(world, player):  # Directly taken from Minecraft's region connection
    # Link mandatory connections first
    for (exit, region) in mandatory_connections:
        world.get_entrance(exit, player).connect(world.get_region(region, player))

    # Get all unpaired exits and all regions without entrances (except the Menu)
    # This function is destructive on these lists.
    exits = [exit.name for r in world.regions if r.player == player for exit in r.exits if
             exit.connected_region is None]
    structs = [r.name for r in world.regions if r.player == player and r.entrances == [] and r.name != 'Menu']
    exits_spoiler = exits[:]  # copy the original order for the spoiler log
    try:
        assert len(exits) == len(structs)
    except AssertionError as e:  # this should never happen
        raise Exception(
            f"Could not obtain equal numbers of Pizza Tower exits and structures for player {player} ({world.player_name[player]})")

    pairs = {}

    def set_pair(exit, struct):
        if (exit in exits) and (struct in structs) and (exit not in illegal_connections.get(struct, [])):
            pairs[exit] = struct
            exits.remove(exit)
            structs.remove(struct)
        else:
            raise Exception(f"Invalid connection: {exit} => {struct} for player {player} ({world.player_name[player]})")

    # Connect plando structures first
    if world.plando_connections[player]:
        for conn in world.plando_connections[player]:
            set_pair(conn.entrance, conn.exit)

    # The algorithm tries to place the most restrictive structures first. This algorithm always works on the
    # relatively small set of restrictions here, but does not work on all possible inputs with valid configurations.
    if world.shuffle_level[player]:
        structs.sort(reverse=True, key=lambda s: len(illegal_connections.get(s, [])))
        for struct in structs[:]:
            try:
                exit = world.random.choice([e for e in exits if e not in illegal_connections.get(struct, [])])
            except IndexError:
                raise Exception(
                    f"No valid structure placements remaining for player {player} ({world.player_name[player]})")
            set_pair(exit, struct)
    else:  # write remaining default connections
        for (exit, struct) in default_connections:
            if exit in exits:
                set_pair(exit, struct)

    # Make sure we actually paired everything; might fail if plando
    try:
        assert len(exits) == len(structs) == 0
    except AssertionError:
        raise Exception(
            f"Failed to connect all Pizza Tower structures for player {player} ({world.player_name[player]})")

    for exit in exits_spoiler:
        world.get_entrance(exit, player).connect(world.get_region(pairs[exit], player))
        if world.shuffle_level[player] or world.plando_connections[player]:
            world.spoiler.set_entrance(exit, pairs[exit], 'entrance', player)


floor_1_regions = [Names.tutorial, Names.entrance, Names.medieval, Names.ruin, Names.dungeon]
floor_2_regions = [Names.badland, Names.graveyard, Names.farm, Names.saloon]
floor_3_regions = [Names.plage, Names.forest, Names.space, Names.minigolf]
floor_4_regions = [Names.street, Names.industrial, Names.sewer, Names.freezer]
floor_5_regions = [Names.chateau, Names.kidsparty, Names.war, Names.tower]

tower_regions = [
    ("Menu", ["New Save"]),
    ("Tower Lobby", [
        "Tower Lobby Stage 0", "Tower Lobby Stage 1", "Tower Lobby Stage 2", "Tower Lobby Stage 3",
        "Tower Lobby Stage 4",
        Names.pepperman + " Stage"]),
    ("Western District", [
        "Western District Stage 1", "Western District Stage 2", "Western District Stage 3", "Western District Stage 4",
        Names.vigilante + " Stage"]),
    ("Vacation Resort", [
        "Vacation Resort Stage 1", "Vacation Resort Stage 2", "Vacation Resort Stage 3", "Vacation Resort Stage 4",
        Names.noise + " Stage"]),
    ("Slum", [
        "Slum Stage 1", "Slum Stage 2", "Slum Stage 3", "Slum Stage 4",
        Names.fakepep + " Stage"]),
    ("Staff Only", [
        "Staff Only Stage 1", "Staff Only Stage 2", "Staff Only Stage 3", "Staff Only Stage 4",
        Names.pizzaface + " Stage"]),
    ("Victory", []),

    (Names.tutorial, []),

    (Names.entrance, []),
    (Names.medieval, []),
    (Names.ruin, []),
    (Names.dungeon, []),

    (Names.badland, []),
    (Names.graveyard, []),
    (Names.farm, []),
    (Names.saloon, []),

    (Names.plage, []),
    (Names.forest, []),
    (Names.space, []),
    (Names.minigolf, []),

    (Names.street, []),
    (Names.industrial, []),
    (Names.sewer, []),
    (Names.freezer, []),

    (Names.chateau, []),
    (Names.kidsparty, []),
    (Names.war, []),
    (Names.tower, []),
]

mandatory_connections = {
    ("New Save", "Tower Lobby"),
    (Names.pepperman + " Stage", "Western District"),
    (Names.vigilante + " Stage", "Vacation Resort"),
    (Names.noise + " Stage", "Slum"),
    (Names.fakepep + " Stage", "Staff Only"),
    (Names.pizzaface + " Stage", "Victory"),

    ("Tower Lobby Stage 0", Names.tutorial),
    ("Staff Only Stage 4", Names.tower),
}

default_connections = [
    ("Tower Lobby Stage 1", Names.entrance),
    ("Tower Lobby Stage 2", Names.medieval),
    ("Tower Lobby Stage 3", Names.ruin),
    ("Tower Lobby Stage 4", Names.dungeon),

    ("Western District Stage 1", Names.badland),
    ("Western District Stage 2", Names.graveyard),
    ("Western District Stage 3", Names.farm),
    ("Western District Stage 4", Names.saloon),

    ("Western District Stage 1", Names.badland),
    ("Western District Stage 2", Names.graveyard),
    ("Western District Stage 3", Names.farm),
    ("Western District Stage 4", Names.saloon),

    ("Vacation Resort Stage 1", Names.plage),
    ("Vacation Resort Stage 2", Names.forest),
    ("Vacation Resort Stage 3", Names.space),
    ("Vacation Resort Stage 4", Names.minigolf),

    ("Slum Stage 1", Names.street),
    ("Slum Stage 2", Names.industrial),
    ("Slum Stage 3", Names.sewer),
    ("Slum Stage 4", Names.freezer),

    ("Staff Only Stage 1", Names.chateau),
    ("Staff Only Stage 2", Names.kidsparty),
    ("Staff Only Stage 3", Names.war)
]

illegal_connections = {}
