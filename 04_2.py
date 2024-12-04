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


def read_left(data, y, x):
    if read(data, y-1, x-1) == 'M' and read(data, y+1, x+1) == 'S':
        return True
    if read(data, y-1, x-1) == 'S' and read(data, y+1, x+1) == 'M':
        return True
    return False


def read_right(data, y, x):
    if read(data, y-1, x+1) == 'M' and read(data, y+1, x-1) == 'S':
        return True
    if read(data, y-1, x+1) == 'S' and read(data, y+1, x-1) == 'M':
        return True
    return False


def read_x(data, y, x):
    if read(data, y, x) == 'A':
        return read_left(data, y, x) and read_right(data, y, x)
    return False


t = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        t += read_x(data, y, x)
print(t)
