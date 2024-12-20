data = """##########
#..O..O.O#
#......O.#
#.OO..O.O#
#..O@..O.#
#O#..O...#
#O..O..O.#
#.OO.O.OO#
#....O...#
##########

<vv>^<v^>v>^vv^v>v<>v^v<v<^vv<<<^><<><>>v<vvv<>^v^>^<<<><<v<<<v^vv^v>^
vvv<<^>^v^^><<>>><>^<<><^vv^^<>vvv<>><^^v>^>vv<>v<<<<v<^v>^<^^>>>^<v<v
><>vv>v^v^<>><>>>><^^>vv>v<^^^>>v^v^<^^>v^^>v^<^v>v<>>v^v^<v>v^^<^^vv<
<<v<^>>^^^^>>>v^<>vvv^><v<<<>^^^vv^<vvv>^>v<^^^^v<>^>vvvv><>>v^<<^^^^^
^><^><>>><>^^<<^^v>>><^<v>^<vv>>v>>>^v><>^v><<<<v>>v<v<v>vvv>^<><<>^><
^>><>^v<><^vvv<^^<><v<<<<<><^v<<<><<<^^<v<^^^><^>>^<v^><<<^>>^v<v^v<v^
>^>>^v>vv>^<<^v<>><<><<v<<v><>v<^vv<<<>^^v^>^^>>><<^v>>v^v><^^>>^<>vv^
<><^^>^^^<><vvvvv^v<v<<>^v<v>v<<^><<><<><<<^^<<<^<<>><<><^^^>^^<>^>v<>
^^>vv<^v^v<vv>^<><v<^v>^^^>>>^^vvv^>vvv<>>>^<^>>>>>^<<^v>^vvv<>^<><<v>
v^^>>><<^^<>>^v^<v^vv<>v^<<>^<^v^v><^<<<><<^<v><v<>vv>>v><v^<vv<>v^<<^"""

with open('Input/15.txt', 'r') as file:
    data = file.read()


WALL = '#'
BOX = 'O'
EMPTY = '.'
ROBOT = '@'

def get_tile(_map, position):
    x, y = position
    if not in_bounds(_map, position):
        return WALL
    return _map[y][x]

def set_tile(_map, position, value):
    x, y = position
    if not in_bounds(_map, position):
        return
    _map[y] = _map[y][:x] + value + _map[y][x+1:]

def in_bounds(_map, position):
    x, y = position
    return 0 <= x < len(_map[0]) and 0 <= y < len(_map)

def direction_to_position(position, direction):
    x, y = position
    if direction == '^':
        return (x, y-1)
    if direction == 'v':
        return (x, y+1)
    if direction == '<':
        return (x-1, y)
    if direction == '>':
        return (x+1, y)
    return position

def move(_map, from_position, direction):
    to_position = direction_to_position(from_position, direction)
    to_tile = get_tile(_map, to_position)
    if to_tile == WALL:
        return False
    if to_tile == BOX:
        if not move(_map, to_position, direction):
            return False
    set_tile(_map, to_position, BOX)
    set_tile(_map, from_position, EMPTY)
    return True

def calculate_score(_map):
    t = 0
    for y in range(len(_map)):
        for x in range(len(_map[y])):
            if get_tile(_map, (x, y)) == BOX:
                t += (y * 100) + (x)
    return t

_map, instructions = data.split('\n\n')
_map = _map.strip().split('\n')
robot_position = None
for y in range(len(_map)):
    for x in range(len(_map[y])):
        if get_tile(_map,(x,y)) == ROBOT:
            robot_position = (y, x)
            set_tile(_map, robot_position, EMPTY)
            break
    if robot_position:
        break
instructions = instructions.replace('\n', '')
print(_map)
print(instructions)


for instruction in instructions:
    if move(_map, robot_position, instruction):
        robot_position = direction_to_position(robot_position, instruction)
set_tile(_map, robot_position, ROBOT)
print('\n'.join(_map))
print(calculate_score(_map))