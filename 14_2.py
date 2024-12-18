import time

data = """p=0,4 v=3,-3
p=6,3 v=-1,-3
p=10,3 v=-1,2
p=2,0 v=2,-1
p=0,0 v=1,3
p=3,0 v=-2,-2
p=7,6 v=-1,-3
p=3,0 v=-1,-2
p=9,3 v=2,3
p=7,3 v=-1,2
p=2,4 v=2,-3
p=9,5 v=-3,-3"""
width, height = 11, 7

with open("Input/14.txt", "r") as file:
    data = file.read()
width, height = 101, 103

# Position = tuple[x, y]
# Velocity = tuple[x, y]
# Robot = tuple[Position, Velocity]

def parse_data(data):
    robots = []
    for line in data.strip().split("\n"):
        parts = line.split(" ")
        parts = [part.split('=')[1] for part in parts]
        x,y = tuple(map(int, parts[0].split(",")))
        position = (x, y)
        x,y = tuple(map(int, parts[1].split(",")))
        velocity = (x, y)
        robots.append([position, velocity])
    return robots

def simulate(robots, width, height):
    for robot in robots:
        x, y = robot[0]
        vx, vy = robot[1]
        x += vx
        while x < 0:
            x += width
        while x >= width:
            x -= width
        y += vy
        while y < 0:
            y += height
        while y >= height:
            y -= height
        robot[0] = (x, y)
    return robots

def print_map(robots, width, height):
    map = [["." for _ in range(width)] for _ in range(height)]
    for robot in robots:
        x, y = robot[0]
        map[y][x] = "#"
    full = '\n'.join([''.join(row) for row in map])
    #for row in map:
    #    print("".join(row))
    print(full)
    
def have_any_overlap(robots, width, height):
    map = [[0 for i in range(width)] for j in range(height)]
    for robot in robots:
        x, y = robot[0]
        map[y][x] += 1
    for row in map:
        for cell in row:
            if cell > 1:
                return True
    return False


data = parse_data(data)
#print_map(data, width, height)
i = 0
while True:
    i += 1
    data = simulate(data,width,height)
    if not have_any_overlap(data, width, height):
        print_map(data, width, height)
        print(i)
        input("Press Enter to continue...")