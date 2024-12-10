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


def search(data, y, x, target, list: set):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
        return
    this = data[y][x]
    if target == this:
        if this == 9:
            list.add((y, x))
            return
        target += 1
        search(data, y+1, x, target, list)
        search(data, y-1, x, target, list)
        search(data, y, x+1, target, list)
        search(data, y, x-1, target, list)
    else:
        return


total = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        if data[y][x] == 0:
            l = set()
            search(data, y, x, 0, l)
            total += len(l)
print(total)
