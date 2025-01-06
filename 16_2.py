# Holy smokes, this was hard.
# Guess it was just adding a lowest cost seen to every position (from position to position)
# and then checking if the cost was higher than the lowest cost seen.

data = """#################
#...#...#...#..E#
#.#.#.#.#.#.#.#.#
#.#.#.#...#...#.#
#.#.#.#.###.#.#.#
#...#.#.#.....#.#
#.#.#.#.#.#####.#
#.#...#.#.#.....#
#.#.#####.#.###.#
#.#.#.......#...#
#.#.###.#####.###
#.#.#...#.....#.#
#.#.#.#####.###.#
#.#.#.........#.#
#.#.#.#########.#
#S#.............#
#################"""

with open("Input/16.txt") as f:
    data = f.read()

_map = data.splitlines()

EMPTY = '.'
WALL = '#'
START = 'S'
END = 'E'

# region Map control


def get_tile(_map, position):
    x, y = position
    if x < 0 or x >= len(_map[0]) or y < 0 or y >= len(_map):
        return WALL
    return _map[y][x]


def is_solid(_map, position):
    return get_tile(_map, position) == WALL


def set_tile(_map, position, value):
    x, y = position
    _map[y] = _map[y][:x] + value + _map[y][x+1:]


def print_map(_map, positions=[], marker='O'):
    _map = _map.copy()
    for x, y in positions:
        set_tile(_map, (x, y), marker)
    print('\n'.join(_map))


# endregion

# region Find start and end
start = None
end = None
for y in range(len(_map)):
    for x in range(len(_map[y])):
        if _map[y][x] == START:
            start = (x, y)
            set_tile(_map, start, EMPTY)
        if _map[y][x] == END:
            end = (x, y)
            set_tile(_map, end, EMPTY)
# endregion

# region Find neighbors


def get_neighbors(position):
    """Returns a list of all empty neighbors of a position"""
    x, y = position
    neighbors = []
    for pos in [(x, y-1), (x+1, y), (x-1, y), (x, y+1)]:
        if get_tile(_map, pos) == EMPTY:
            neighbors.append(pos)
    return neighbors


def get_neighbor_costs(position, previous):
    """Returns a list of all empty neighbors of a position and turning costs"""
    x, y = position
    north = (x, y-1)
    east = (x+1, y)
    south = (x, y+1)
    west = (x-1, y)
    neighbors = []
    if position[0] == previous[0]:  # horizontal
        if position[1] > previous[1]:  # south
            # print('South')
            if not is_solid(_map, south):
                neighbors.append((south, 1))
            if not is_solid(_map, east):
                neighbors.append((east, 1000))
            if not is_solid(_map, west):
                neighbors.append((west, 1000))
        else:  # north
            # print('North')
            if not is_solid(_map, north):
                neighbors.append((north, 1))
            if not is_solid(_map, east):
                neighbors.append((east, 1000))
            if not is_solid(_map, west):
                neighbors.append((west, 1000))
    else:  # vertical
        if position[0] > previous[0]:  # east
            # print('East')
            if not is_solid(_map, east):
                neighbors.append((east, 1))
            if not is_solid(_map, north):
                neighbors.append((north, 1000))
            if not is_solid(_map, south):
                neighbors.append((south, 1000))
        else:  # west
            # print('West')
            if not is_solid(_map, west):
                neighbors.append((west, 1))
            if not is_solid(_map, north):
                neighbors.append((north, 1000))
            if not is_solid(_map, south):
                neighbors.append((south, 1000))
    return neighbors

# endregion

# region Find junctions


def is_junction(map, position):
    if is_solid(map, position):
        return False
    return len(get_neighbors(position)) > 2

# endregion


position_lowest_cost = {}
# ((x,y),(x,y)): lowest_cost
paths = []
queue = [(start, (start[0]-1, start[1]), 0, set())]

while queue:
    current, previous, cost, visited = queue.pop(0)
    # print('Current:', current, 'Previous:', previous, 'Cost:', cost, 'Visited:', len(visited))
    visited.add(current)

    if current == end:
        # print('End found:', cost)
        paths.append((cost, visited))
        continue

    is_first = True
    for neighbor_position, neighbor_cost in get_neighbor_costs(current, previous):
        if neighbor_position in visited:
            continue
        # Have to check for junctions here, because the corner cost messes with the cost calculation
        if not is_junction(_map, neighbor_position):
            if neighbor_position in position_lowest_cost:
                if cost + neighbor_cost > position_lowest_cost[neighbor_position]:
                    continue
                position_lowest_cost[neighbor_position] = cost + neighbor_cost
            else:
                position_lowest_cost[neighbor_position] = cost + neighbor_cost
        # This is so that the visited set is not shared between paths and we can reuse the first visited set
        if is_first:
            is_first = False
        else:
            visited = visited.copy()

        queue.append((neighbor_position, current, cost + neighbor_cost, visited))


paths.sort(key=lambda x: x[0])
lowest_cost = paths[0][0]
all_positions = set()
for cost, path in paths:
    if cost > lowest_cost:
        break
    all_positions.update(path)
# print_map(_map, all_positions, 'O')
print(len(all_positions))
