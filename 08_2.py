data = """............
........0...
.....0......
.......0....
....0.......
......A.....
............
............
........A...
.........A..
............
............""".splitlines()

with open('Input/08.txt') as f:
    data = f.read().splitlines()


bounds = (len(data), len(data[0]))
antennas = dict()  # {A: [(y, x), (y, x), ...]}

for y in range(len(data)):
    for x in range(len(data[y])):
        a = data[y][x]
        if a != '.':
            if antennas.get(a) == None:
                antennas[a] = []
            antennas[a].append((y, x))

antinodes = set()  # ((y, x), (y, x), ...)


def add_antinodes(y, x, y_dist, x_dist):
    while (True):
        y += y_dist
        x += x_dist
        if y < 0 or x < 0 or y >= bounds[0] or x >= bounds[1]:
            break
        antinodes.add((y, x))


for a in antennas:
    l = antennas[a]
    for i in range(len(l)):
        for j in range(i + 1, len(l)):
            y1, x1 = l[i]
            y2, x2 = l[j]
            # print(y1, x1, y2, x2)
            y_dist = y2 - y1
            x_dist = x2 - x1
            # print(y_dist, x_dist)
            add_antinodes(y1, x1, y_dist, x_dist)
            add_antinodes(y2, x2, -y_dist, -x_dist)


# print(antennas)
# print(antinodes)

print(len(antinodes))
