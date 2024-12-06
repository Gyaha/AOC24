with open('Input/input06.txt') as file:
    data = file.readlines()

test_data = """....#.....
.........#
..........
..#.......
.......#..
..........
.#..^.....
........#.
#.........
......#...""".splitlines()

# data = test_data


guard = '^'
blocked = '#'
open_space = '.'


def find_guard(data) -> tuple[int, int]:
    for y in range(len(data)):
        for x in range(len(data[y])):
            if data[y][x] == guard:
                return y, x
    return None


def get_tile(data, position) -> str:
    return get_tile_cord(data, position[0], position[1])


def get_tile_cord(data, y, x) -> str:
    if 0 <= y and y < len(data) and 0 <= x and x < len(data[y]):
        return data[y][x]
    return None


def get_next_position(position, direction) -> tuple[int, int]:
    y, x = position
    if direction == 'north':
        return y - 1, x
    elif direction == 'east':
        return y, x + 1
    elif direction == 'south':
        return y + 1, x
    elif direction == 'west':
        return y, x - 1
    return None


def turn_right(direction) -> str:
    if direction == 'north':
        return 'east'
    elif direction == 'east':
        return 'south'
    elif direction == 'south':
        return 'west'
    elif direction == 'west':
        return 'north'
    return None


def test_obstacle(data, obstacle_position):
    guard_direction = 'north'               # north, east, south, west
    seen = set()                            # [(y, x, dir), ...]
    guard_position = find_guard(data)       # (y, x)
    while True:
        seen_position_and_direction = (guard_position[0], guard_position[1], guard_direction)
        if seen_position_and_direction in seen:
            print('Loop', obstacle_position)
            return True
        seen.add(seen_position_and_direction)
        next_position = get_next_position(guard_position, guard_direction)
        next_tile = get_tile(data, next_position)
        if next_tile == blocked or next_position == obstacle_position:
            # print('Blocked', next_position)
            guard_direction = turn_right(guard_direction)
            continue
        elif next_tile == None:
            # print('Out of bounds')
            return False
        guard_position = next_position


working_obstacles = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        obstacle_position = (y, x)
        if get_tile(data, obstacle_position) == open_space:
            working_obstacles += test_obstacle(data, obstacle_position)


print(working_obstacles)
