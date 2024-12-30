data = """029A
980A
179A
456A
379A"""

with open('Input/21.txt', 'r') as file:
    data = file.read()

codes = data.splitlines()

# 1 2 3
# 4 5 6
# 7 8 9
#   0 A
numpad_paths = {}
numpad_keys = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', 'A']
numpad_map = [
    ['7', '8', '9'],
    ['4', '5', '6'],
    ['1', '2', '3'],
    [' ', '0', 'A']
]

#   ^ A
# < v >
directional_paths = {}
directional_keys = ['^', '>', 'v', '<', 'A']
directional_map = [
    [' ', '^', 'A'],
    ['<', 'v', '>']
]

org_directions = [
    '029A: <vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A',
    '980A: <v<A>>^AAAvA^A<vA<AA>>^AvAA<^A>A<v<A>A>^AAAvA<^A>A<vA>^A<A>A',
    '179A: <v<A>>^A<vA<A>>^AAvAA<^A>A<v<A>>^AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A',
    '456A: <v<A>>^AA<vA<A>>^AAvAA<^A>A<vA>^A<A>A<vA>^A<A>A<v<A>A>^AAvA<^A>A',
    '379A: <v<A>>^AvA^A<vA<AA>>^AAvA<^A>AAvA^A<vA>^AA<A>A<v<A>A>^AAAvA<^A>A'
]


def is_key(position, _map):
    x, y = position
    if y < 0 or y >= len(_map) or x < 0 or x >= len(_map[y]):
        return False
    return _map[y][x] != ' '


def get_neighbours(position, _map):
    x, y = position
    neighbours = []
    if is_key((x, y - 1), _map):
        neighbours.append(((x, y - 1), '^'))
    if is_key((x + 1, y), _map):
        neighbours.append(((x + 1, y), '>'))
    if is_key((x, y + 1), _map):
        neighbours.append(((x, y + 1), 'v'))
    if is_key((x - 1, y), _map):
        neighbours.append(((x - 1, y), '<'))
    return neighbours


def find_all_paths(start_key, end_key, _map):
    paths = []

    # region Find start and end positions
    start_position = None
    end_position = None
    for y, row in enumerate(_map):
        for x, key in enumerate(row):
            if key == start_key:
                start_position = (x, y)
            if key == end_key:
                end_position = (x, y)
    # endregion

    queue = [(start_position, [], [])]
    while len(queue):
        position, path, visited = queue.pop(0)
        x, y = position

        if position == end_position:
            paths.append(''.join(path) + 'A')
            continue

        for next_position, direction in get_neighbours(position, _map):
            if next_position in visited:
                continue
            queue.append((next_position, path + [direction], visited + [position]))
    return paths


def get_shortest_paths(paths):
    shortest = int(1e9)
    shortest_paths = []
    for path in paths:
        if len(path) < shortest:
            shortest = len(path)
            shortest_paths = [path]
        elif len(path) == shortest:
            shortest_paths.append(path)
    return shortest_paths

# region Cache all paths


for key_1 in numpad_keys:
    for key_2 in numpad_keys:
        numpad_paths[(key_1, key_2)] = get_shortest_paths(find_all_paths(key_1, key_2, numpad_map))

for key_1 in directional_keys:
    for key_2 in directional_keys:
        directional_paths[(key_1, key_2)] = get_shortest_paths(find_all_paths(key_1, key_2, directional_map))
# endregion


def build_all_paths(code, pointer, path='', path_cache={}):
    if pointer == len(code):
        return [path]

    if pointer == 0:
        current_key = 'A'
        next_key = code[pointer]
    else:
        current_key = code[pointer - 1]
        next_key = code[pointer]

    paths = []
    if (current_key, next_key) not in path_cache:
        print('Cache:', path_cache)
        print('Missing path:', current_key, next_key)
        quit()
    for next_path in path_cache[(current_key, next_key)]:
        paths += build_all_paths(code, pointer + 1, path + next_path, path_cache)
    return paths


def press_code(code):
    possible_paths = []
    first_paths = get_shortest_paths(build_all_paths(code, 0, '', numpad_paths))
    # print('First paths:', len(first_paths))
    # print(first_paths[0])
    for first_path in first_paths:
        # print('A:', first_path)
        second_paths = get_shortest_paths(build_all_paths(first_path, 0, '', directional_paths))
        # print(second_paths[0])
        # print('Second paths:', len(second_paths))
        for second_path in second_paths:
            # print(' B:', second_path)
            third_paths = get_shortest_paths(build_all_paths(second_path, 0, '', directional_paths))
            # print(third_paths[0])
            # print('Third paths:', len(third_paths))
            # for third_path in third_paths:
            #    print('  C:', third_path)
            possible_paths += third_paths
    return possible_paths


total = 0
for code in codes:
    path = get_shortest_paths(press_code(code))[0]
    length = len(path)
    numeric_code = int(code[:-1])
    complexity = length * numeric_code
    total += complexity
    print(code, path, length, numeric_code, complexity)
print('Total:', total)
