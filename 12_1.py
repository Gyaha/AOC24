data = """RRRRIICCFF
RRRRIICCCF
VVRRRCCFFF
VVRCCCJFFF
VVVVCJJCFE
VVIVCCJJEE
VVIIICJJEE
MIIIIIJJEE
MIIISIJEEE
MMMISSJEEE"""
data = """OOOOO
OXOXO
OOOOO
OXOXO
OOOOO"""
data = """AAAA
BBCD
BBCC
EEEC"""
data = data.split('\n')

with open('Input/12.txt', 'r') as file:
    data = file.read().split('\n')

def get_tile(y:int, x:int):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
        return None
    return data[y][x]

def rec_check_area(y:int, x:int, target:str, visited:set):
    if (y, x) in visited:
        return
    if get_tile(y, x) == target:
        visited.add((y, x))
        rec_check_area(y-1, x,target,  visited)
        rec_check_area(y+1, x, target, visited)
        rec_check_area(y, x-1,target,  visited)
        rec_check_area(y, x+1, target, visited)

def calc_price(y:int, x:int):
    t = get_tile(y, x)
    s = 0
    if get_tile(y + 1,x) != t:
        s += 1
    if get_tile(y - 1,x) != t:
        s += 1
    if get_tile(y,x + 1) != t:
        s += 1
    if get_tile(y,x - 1) != t:
        s += 1
    if s == 0:
        return 0
    a = set()
    rec_check_area(y, x, t, a)
    return len(a) * s

total = 0
for y in range(len(data)):
    for x in range(len(data[y])):
        total += calc_price(y, x)
print(total)