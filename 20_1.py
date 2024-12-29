data = """###############
#...#...#.....#
#.#.#.#.#.###.#
#S#...#.#.#...#
#######.#.#.###
#######.#.#...#
#######.#.###.#
###..E#...#...#
###.#######.###
#...###...#...#
#.#####.#.###.#
#.#...#.#.#...#
#.#.#.#.#.#.###
#...#...#...###
###############"""

with open("Input/20.txt", "r") as f:
    data = f.read()

_map = data.splitlines()


def print_map(_map, points=[], marker="X"):
    _map_copy = _map.copy()
    for x, y in points:
        set_tile(_map_copy, x, y, marker)
    for line in _map_copy:
        print(line)


def copy_map(_map):
    return [line for line in _map]


def is_solid(_map, x, y):
    if x < 0 or y < 0 or x >= len(_map[0]) or y >= len(_map):
        return True
    return _map[y][x] == "#"


def set_tile(_map, x, y, c):
    _map[y] = _map[y][:x] + c + _map[y][x + 1:]


def get_tile(_map, x, y):
    return _map[y][x]


# region Find start and end
start, end = None, None
for y in range(len(_map)):
    for x in range(len(_map[y])):
        if get_tile(_map, x, y) == "S":
            start = (x, y)
            set_tile(_map, x, y, ".")
        if get_tile(_map, x, y) == "E":
            end = (x, y)
            set_tile(_map, x, y, ".")
# endregion

# region Find walls that can be used to cheat


def is_cheat(_map, x, y):
    if not is_solid(_map, x, y):
        return False
    if (not is_solid(_map, x - 1, y) and not is_solid(_map, x + 1, y)) or (not is_solid(_map, x, y - 1) and not is_solid(_map, x, y + 1)):
        return True
    return False


cheats = set()
for y in range(len(_map)):
    for x in range(len(_map[y])):
        if is_cheat(_map, x, y):
            cheats.add((x, y))

print('Cheats:', len(cheats))
# endregion

# region Pathfinding


def find_shortest_path(_map, start, end):
    queue = [(start, 0)]
    visited = set()
    while queue:
        (x, y), steps = queue.pop(0)
        if (x, y) == end:
            return steps
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            if is_solid(_map, x + dx, y + dy):
                continue
            queue.append(((x + dx, y + dy), steps + 1))
    return -1


# endregion

# Find the shortest path without cheating
shortest_path = find_shortest_path(_map, start, end)

# Find the shortest path for each cheat
possible_cheats = []
for cheat in cheats:
    _map_copy = copy_map(_map)
    set_tile(_map_copy, cheat[0], cheat[1], ".")
    cost = find_shortest_path(_map_copy, start, end)
    if cost != -1:
        possible_cheats.append(shortest_path - cost)


# Count cheats that save at least 100 steps
t = 0
for x in possible_cheats:
    if x >= 100:
        t += 1
print(t)
