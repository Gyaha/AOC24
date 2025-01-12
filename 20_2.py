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


def get_distance_manhatten(start, end):
    return abs(start[0] - end[0]) + abs(start[1] - end[1])


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


def get_distance_from(target):
    distance_from = {target: 0}
    queue = [target]
    visited = set()
    while queue:
        x, y = queue.pop(0)
        visited.add((x, y))
        my_distance = distance_from[(x, y)]
        for dx, dy in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if is_solid(_map, new_x, new_y) or (new_x, new_y) in visited:
                continue
            distance_from[(new_x, new_y)] = my_distance + 1
            queue.append((new_x, new_y))
    return distance_from


distance_to_end = get_distance_from(end)
full_distance = distance_to_end[start]

CHEAT_DISTANCE = 20

saves = {}
for position in distance_to_end:
    position_distance_to_end = distance_to_end[position]
    for other_position in distance_to_end:
        # This could be optimized by only checking the ones that are close enough.
        # But this is fast enough.
        if other_position == position:
            continue
        cheat_distance = get_distance_manhatten(position, other_position)
        if cheat_distance > CHEAT_DISTANCE:
            continue
        other_position_distance_to_end = distance_to_end[other_position]
        if position_distance_to_end > other_position_distance_to_end:
            saved = position_distance_to_end - (other_position_distance_to_end + cheat_distance)
            if saved not in saves:
                saves[saved] = 0
            saves[saved] += 1

save_keys = list(saves.keys())
save_keys.sort(reverse=True)
# print(save_keys)

total = 0
for save in save_keys:
    if save < 100:
        break
    total += saves[save]
    # print(save, saves[save])

print(total)
