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

#map_bounds = (101, 103)

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
    map = [["." for i in range(width)] for j in range(height)]
    for robot in robots:
        x, y = robot[0]
        map[y][x] = "#"
    for row in map:
        print("".join(row))
    print()

def calculate_safety_factor(robots, width, height):
    quadrants = [[0,0],[0,0]]
    middle_x = width//2
    middle_y = height//2
    for robot in robots:
        x, y = robot[0]
        if x == middle_x or y == middle_y:
            continue
        if x < width//2:
            if y < height//2:
                quadrants[0][0] += 1
            else:
                quadrants[0][1] += 1
        else:
            if y < height//2:
                quadrants[1][0] += 1
            else:
                quadrants[1][1] += 1
    print(quadrants[0][0], quadrants[0][1], quadrants[1][0], quadrants[1][1] )
    return quadrants[0][0]* quadrants[0][1]* quadrants[1][0]* quadrants[1][1] 
        



data = parse_data(data)
print_map(data, width, height)
for i in range(100):
    data = simulate(data,width,height)
    print_map(data, width, height)
print(calculate_safety_factor(data, width, height))