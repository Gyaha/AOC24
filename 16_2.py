# Looks like this has to be done with a recursive find all.
# That is too slow, so I will try to do it with a iterative find all.
# Still too slow.
# I will try with finding junctions and then find all paths from there.
# That failed as well.
# Now I will try recursive plus caching.
# Still too slow. Tried then to find all paths, planning to sort after. Also too slow.
# Will try the junction approach again.

# Okay this is looking good, but I have a bit of a problem with the cost calculation.
# I have to give up on this for now. Will come back to it later.

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

def get_tile(_map, position):
    x, y = position
    if x < 0 or x >= len(_map[0]) or y < 0 or y >= len(_map):
        return WALL
    return _map[y][x]

def set_tile(_map, position, value):
    x, y = position
    _map[y] = _map[y][:x] + value + _map[y][x+1:]

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

def get_neighbors(position, direction):
    x, y = position
    if direction == 'N':
        return [((x, y-1), 'N'), 
                ((x+1, y), 'E'), 
                ((x-1, y), 'W')]
    if direction == 'E':
        return [((x+1, y), 'E'), 
                ((x, y+1), 'S'),
                ((x, y-1), 'N')]
    if direction == 'S':
        return [((x, y+1), 'S'), 
                ((x+1, y), 'E'), 
                ((x-1, y), 'W')]
    if direction == 'W':
        return [((x-1, y), 'W'), 
                ((x, y+1), 'S'), 
                ((x, y-1), 'N')]
    print('Error: Invalid direction')

def print_map(_map, positions = [], marker = 'O'):
    _map = _map.copy()
    for x, y in positions:
        set_tile(_map, (x, y), marker)
    print('\n'.join(_map))

def find_junction_positions(_map):
    junctions = []
    for y in range(len(_map)):
        for x in range(len(_map[y])):
            if get_tile(_map, (x, y)) == EMPTY:
                neighbors = 0
                for dx, dy in [(0, -1), (1, 0), (0, 1), (-1, 0)]:
                    if get_tile(_map, (x+dx, y+dy)) == EMPTY:
                        neighbors += 1
                if neighbors > 2:
                    junctions.append((x, y))
    return junctions

junction_positions = [start, end] + find_junction_positions(_map)

print_map(_map, junction_positions, 'J')

def get_all_neighbors(position):
    x, y = position
    return [((x, y-1), 'N'), 
            ((x+1, y), 'E'), 
            ((x, y+1), 'S'),
            ((x-1, y), 'W')]

def find_junction_connection(position, direction, cost = 0):
    if get_tile(_map, position) == WALL:
        return None
    if position in junction_positions:
        return position, direction, cost
    for new_position, new_direction in get_neighbors(position, direction):
        new_cost = cost + 1 + (direction != new_direction) * 1000
        connection = find_junction_connection(new_position, new_direction, new_cost)
        if connection:
            return connection
    return None

def find_junction_connections(junction_position):
    connections = []
    for position, direction in get_all_neighbors(junction_position):
        connection = find_junction_connection(position, direction)
        if connection:
            connections.append((direction,connection))
    return connections

junctions = {}
for junction_position in junction_positions:
    junctions[junction_position] = find_junction_connections(junction_position)
    
for junction_position in junctions:
    print(junction_position, '->', junctions[junction_position])
    #print_map(_map, [junction_position] + junctions[junction_position], 'X')

def get_allowed_directions(direction):
    if direction == 'N':
        return ['N', 'E', 'W']
    if direction == 'E':
        return ['E', 'S', 'N']
    if direction == 'S':
        return ['S', 'E', 'W']
    if direction == 'W':
        return ['W', 'S', 'N']
    print('Error: Invalid direction:', direction)
    quit()

def find_path(position, direction, cost = 0, path = [], visited = set()):
    if position == end:
        return path, cost
    visited.add(position)
    allowed_directions = get_allowed_directions(direction)
    for start_direction, (new_position, new_direction, new_cost) in junctions[position]:
        if start_direction not in allowed_directions:
            continue
        if new_position in visited:
            continue
        new_path, new_cost = find_path(new_position, new_direction, cost + new_cost, path + [(new_position, new_direction)], visited)
        
        if new_path:
            new_cost += 1
            if start_direction != direction:
                new_cost += 1000
            return new_path, new_cost
    return None, None
    

path = find_path(start, 'E')
print(path)