data = """89010123
78121874
87430965
96549874
45678903
32019012
01329801
10456732""".splitlines()

with open('Input/10.txt') as f:
    data = f.readlines()

data = [[int(c) for c in line.strip()] for line in data]


def search(data, y, x, target):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
        return 0
    this = data[y][x]
    if target == this:
        if this == 9:
            return 1
        target += 1
        return search(data, y+1, x, target) + search(data, y-1, x, target) + search(data, y, x+1, target) + search(data, y, x-1, target)
    else:
        return 0


total = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 0:
            total += search(data, y, x, 0)
print(total)
