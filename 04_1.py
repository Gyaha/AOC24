phrase = 'XMAS'


with open('Input/input04.txt') as file:
    data = file.readlines()

data_test = [
    'MMMSXXMASM',
    'MSAMXMSMSA',
    'AMXSXMAAMM',
    'MSAMASMSMX',
    'XMASAMXAMM',
    'XXAMMXXAMA',
    'SMSMSASXSS',
    'SAXAMASAAA',
    'MAMMMXMMMM',
    'MXMXAXMASX'
]
# data = data_test


def read(data, y, x):
    if 0 <= y and y < len(data) and 0 <= x and x < len(data[y]):
        return data[y][x]
    return None


def read_right(data, y, x):
    for i, l in enumerate(phrase):
        if read(data, y, x + i) != l:
            return False
    return True


def read_left(data, y, x):
    for i, l in enumerate(phrase):
        if read(data, y, x - i) != l:
            return False
    return True


def read_down(data, y, x):
    for i, l in enumerate(phrase):
        if read(data, y + i, x) != l:
            return False
    return True


def read_up(data, y, x):
    for i, l in enumerate(phrase):
        if read(data, y - i, x) != l:
            return False
    return True


def read_down_right(data, y, x):
    for i, l in enumerate(phrase):
        if read(data, y + i, x + i) != l:
            return False
    return True


def read_down_left(data, y, x):
    for i, l in enumerate(phrase):
        if read(data, y + i, x - i) != l:
            return False
    return True


def read_up_right(data, y, x):
    for i, l in enumerate(phrase):
        if read(data, y - i, x + i) != l:
            return False
    return True


def read_up_left(data, y, x):
    for i, l in enumerate(phrase):
        if read(data, y - i, x - i) != l:
            return False
    return True


t = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        t += read_right(data, y, x)
        t += read_left(data, y, x)
        t += read_down(data, y, x)
        t += read_up(data, y, x)
        t += read_down_right(data, y, x)
        t += read_down_left(data, y, x)
        t += read_up_right(data, y, x)
        t += read_up_left(data, y, x)

print(t)
