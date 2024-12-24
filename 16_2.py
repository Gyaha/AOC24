data = """###############
#.......#....E#
#.#.###.#.###.#
#.....#.#...#.#
#.###.#####.#.#
#.#.#.......#.#
#.#.#####.###.#
#...........#.#
###.#.#####.#.#
#...#.....#.#.#
#.#.#.###.#.#.#
#.....#...#.#.#
#.###.#.#.#.#.#
#S..#.....#...#
###############"""

#with open("Input/16.txt") as f:
#    data = f.read()

_map = data.splitlines()

EMPTY = '.'
WALL = '#'
START = 'S'
END = 'E'

def direction_cost(current_direction, new_direction):
    if current_direction == new_direction:
        return 0
    if current_direction == 'N':
        if new_direction == 'E' or new_direction == 'W':
            return 1000
        return 2000
    if current_direction == 'E':
        if new_direction == 'N' or new_direction == 'S':
            return 1000
        return 2000
    if current_direction == 'S':
        if new_direction == 'E' or new_direction == 'W':
            return 1000
        return 2000
    if current_direction == 'W':
        if new_direction == 'N' or new_direction == 'S':
            return 1000
        return 2000
    print('Error: Invalid direction')

def get_neighbors(node):
    # Returns a list of tuples (x, y, direction, cost)
    neighbors = []
    x, y = node[0]
    direction = node[1]
    cost = node[2]
    neighbors.append(((x,y-1),'N',1+cost+direction_cost(direction, 'N')))
    neighbors.append(((x+1,y),'E',1+cost+direction_cost(direction, 'E')))
    neighbors.append(((x,y+1),'S',1+cost+direction_cost(direction, 'S')))
    neighbors.append(((x-1,y),'W',1+cost+direction_cost(direction, 'W')))
    return neighbors

def direction_to_arrow(direction):
    if direction == 'N':
        return '^'
    if direction == 'E':
        return '>'
    if direction == 'S':
        return 'v'
    if direction == 'W':
        return '<'
    print('Error: Invalid direction')

def get_tile(_map, position):
    x, y = position
    if x < 0 or x >= len(_map[0]) or y < 0 or y >= len(_map):
        return WALL
    return _map[y][x]

# region Find start and end
start = None
end = None
for y in range(len(_map)):
    for x in range(len(_map[y])):
        if _map[y][x] == START:
            start = (x, y)
        if _map[y][x] == END:
            end = (x, y)
# endregion

# (x, y, direction, cost)
to_visit = [(start,'E',0)]
# old::: {(x,y): (direction, cost)}
# {(x,y): cost, [direction, ...] }
visited = {}
while len(to_visit) > 0:
    current = to_visit.pop(0)

    position = current[0]
    direction = current[1]
    cost = current[2]

    tile = get_tile(_map, position)

    if tile == WALL:
        continue

    if position in visited:
        if visited[position][0] == cost:
            print('Merge')
            if not direction in visited[position][1]:
                visited[position][1].append(direction)
        elif visited[position][0] < cost:
            #print('Skip')
            continue
        elif visited[position][0] > cost:
            #print('Overwrite')
            visited[position] = (cost, [direction])
    else:
        visited[position] = (cost, [direction])
    #visited[position] = (current[1], current[2])
    to_visit += get_neighbors(current)


# region Print map
for v in visited:
    val = visited[v]
    x, y = v
    if len(val[1]) > 1:
        _map[y] = _map[y][:x] + 'X' + _map[y][x+1:]
    else:
        _map[y] = _map[y][:x] + direction_to_arrow (val[1][0]) + _map[y][x+1:]
print('\n'.join(_map))
# endregion

print(visited[end][0])