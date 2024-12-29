data = """5,4
4,2
4,5
3,0
2,1
6,3
2,4
1,5
0,6
3,3
2,6
5,1
1,2
5,5
2,5
6,5
1,4
0,4
6,4
1,1
6,1
1,0
0,5
1,6
2,0"""

with open("Input/18.txt", "r") as f:
    data = f.read()

data = data.strip().split("\n")

walls = set()

for i in range(len(data)):
    data[i] =  [int(d) for d in data[i].split(",")]

def add_walls(_from, _to, walls, data):
    for i in range(_from, _to):
        walls.add((data[i][0], data[i][1]))

add_walls(0, 1024, walls, data)

def is_wall(x, y, width, height, walls):
    if x < 0 or x >= width:
        return True
    if y < 0 or y >= height:
        return True
    return (x, y) in walls

def print_map(width, height, walls):
    for y in range(height):
        for x in range(width):
            if is_wall(x, y, width, height, walls):
                print("#", end="")
            else:
                print(".", end="")
        print()

def path_find(start, end, width, height, walls) -> int:
    queue = [(start, 0)]
    visited = set()
    while queue:
        pos, dist = queue.pop(0)
        if pos == end:
            return dist
        if pos in visited:
            continue
        visited.add(pos)
        x, y = pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_pos = (x + dx, y + dy)
            if is_wall(new_pos[0], new_pos[1], width, height, walls):
                continue
            queue.append((new_pos, dist + 1))
    return -1

print(path_find((0, 0), (70, 70), 71, 71, walls))

for i in range(len(data)):
    walls = set()
    add_walls(0, i, walls, data)
    cost = path_find((0, 0), (70, 70), 71, 71, walls)
    #print(i, cost)
    if cost == -1:
        print(','.join([str(d) for d in data[i-1]]))
        break