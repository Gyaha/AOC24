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
            y1_anti = y1 - y_dist
            x1_anti = x1 - x_dist
            # print(y1_anti, x1_anti)
            y2_anti = y2 + y_dist
            x2_anti = x2 + x_dist
            # print(y2_anti, x2_anti)
            antinodes.add((y1_anti, x1_anti))
            antinodes.add((y2_anti, x2_anti))


# print(antennas)
# print(antinodes)

total = 0
for an in antinodes:
    y, x = an
    if y < 0 or x < 0 or y >= bounds[0] or x >= bounds[1]:
        continue
    total += 1

print(total)
