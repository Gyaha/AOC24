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

#data = 
"""#######
#...#.#
#.....#
#..OO@#
#..O..#
#.....#
#######

vv<<<^^<<^^"""

with open('Input/15.txt', 'r') as file:
    data = file.read()




WALL = '#'
BOX_LEFT = '['
BOX_RIGHT = ']'
BOX = [BOX_LEFT, BOX_RIGHT]
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

def swap_tiles(_map, from_position, to_position):
    tile1 = get_tile(_map, from_position)
    tile2 = get_tile(_map, to_position)
    set_tile(_map, from_position, tile2)
    set_tile(_map, to_position, tile1)

def in_bounds(_map, position):
    x, y = position
    return 0 <= x < len(_map[0]) and 0 <= y < len(_map)

def position_in_direction(position, direction):
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

def is_direction_vertical(direction):
    return direction in ['^', 'v']

def can_move(_map, from_position, direction, check_sides=True):
    from_tile = get_tile(_map, from_position)
    to_position = position_in_direction(from_position, direction)
    to_tile = get_tile(_map, to_position)
    if to_tile == WALL:
        return False
    if check_sides and is_direction_vertical(direction):
        if from_tile == BOX_LEFT:
            if not can_move(_map, position_in_direction(from_position, '>'), direction, False):
                return False
        elif from_tile == BOX_RIGHT:
            if not can_move(_map, position_in_direction(from_position, '<'), direction, False):
                return False
    if to_tile in BOX:
        if not can_move(_map, to_position, direction):
            return False
    return True
    

def move(_map, from_position, direction):
    to_position = position_in_direction(from_position, direction)
    to_tile = get_tile(_map, to_position)

    if to_tile == WALL:
        return False
    if to_tile in BOX:
        if is_direction_vertical(direction):
            if to_tile is BOX_LEFT:
                move(_map, position_in_direction(to_position, '>'), direction)
            elif to_tile is BOX_RIGHT:  
                move(_map, position_in_direction(to_position, '<'), direction)
        move(_map, to_position, direction)
    swap_tiles(_map, from_position, to_position)
    return True


def calculate_score(_map):
    t = 0
    for y in range(len(_map)):
        for x in range(len(_map[y])):
            if get_tile(_map, (x, y)) == BOX_LEFT:
                t += (y * 100) + (x)
    return t

_map, instructions = data.split('\n\n')
_map = _map.strip().split('\n')
instructions = instructions.replace('\n', '')

WALL_OLD = '#'
WALL_NEW = '##'
BOX_OLD = 'O'
BOX_NEW = '[]'
EMPTY_OLD = '.'
EMPTY_NEW = '..'
ROBOT_OLD = '@'
ROBOT_NEW = '@.'

for i, line in enumerate(_map):
    line = line.replace(WALL_OLD, WALL_NEW)
    line = line.replace(BOX_OLD, BOX_NEW)
    line = line.replace(EMPTY_OLD, EMPTY_NEW)
    line = line.replace(ROBOT_OLD, ROBOT_NEW)
    _map[i] = line

robot_position = None
for y in range(len(_map)):
    for x in range(len(_map[y])):
        if get_tile(_map,(x, y)) == ROBOT:
            robot_position = (x, y)
            set_tile(_map, robot_position, EMPTY)
            break
    if robot_position:
        break

print('\n'.join(_map))

for instruction in instructions:
    if can_move(_map, robot_position, instruction):
        move(_map, robot_position, instruction)
        robot_position = position_in_direction(robot_position, instruction)
    #if move(_map, robot_position, instruction):
    #    robot_position = position_in_direction(robot_position, instruction)
    set_tile(_map, robot_position, instruction)
    #print('\n'.join(_map))
    set_tile(_map, robot_position, EMPTY)
    #input()

set_tile(_map, robot_position, ROBOT)
print('\n'.join(_map))

print(calculate_score(_map))