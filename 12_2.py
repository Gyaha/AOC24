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

data = data.split('\n')

with open('Input/12.txt', 'r') as file:
    data = file.read().split('\n')

def get_tile(y:int, x:int):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
        return None
    return data[y][x]

def is_top_left(y:int, x:int):
    t = get_tile(y, x)
    # Above is the same
    if get_tile(y-1, x) == t:
        return False
    # Left is the same
    if get_tile(y, x - 1) == t:
        return False
    return True

def is_bottom_right(y:int, x:int):
    t = get_tile(y, x)
    # Below is the same
    if get_tile(y+1, x) == t:
        return False
    # Right is the same
    if get_tile(y, x + 1) == t:
        return False
    return True

def is_top_right(y:int, x:int):
    t = get_tile(y, x)
    # Above is the same
    if get_tile(y-1, x) == t:
        return False
    # Right is the same
    if get_tile(y, x + 1) == t:
        return False
    return True

def is_bottom_left(y:int, x:int):
    t = get_tile(y, x)
    # Below is the same
    if get_tile(y+1, x) == t:
        return False
    # Left is the same
    if get_tile(y, x - 1) == t:
        return False
    return True

def is_convex_top_left(y:int, x:int):
    # OX.
    # XT.
    # ...
    t = get_tile(y, x)
    if get_tile(y-1, x) != t:
        return False
    if get_tile(y, x-1) != t:
        return False
    if get_tile(y-1, x-1) == t:
        return False
    return True
 
def is_convex_bottom_right(y:int, x:int):
    # ...
    # .TX
    # .XO
    t = get_tile(y, x)
    if get_tile(y+1, x) != t:
        return False
    if get_tile(y, x+1) != t:
        return False
    if get_tile(y+1, x+1) == t:
        return False
    return True

def is_convex_top_right(y:int, x:int):
    # .XO
    # .TX
    # ...
    t = get_tile(y, x)
    if get_tile(y-1, x) != t:
        return False
    if get_tile(y, x+1) != t:
        return False
    if get_tile(y-1, x+1) == t:
        return False
    return True

def is_convex_bottom_left(y:int, x:int):
    # ...
    # XT.
    # OX.
    t = get_tile(y, x)
    if get_tile(y+1, x) != t:
        return False
    if get_tile(y, x-1) != t:
        return False
    if get_tile(y+1, x-1) == t:
        return False
    return True
  
def corner_count(y:int, x:int):
    count = 0
    if is_top_left(y, x):
        count += 1
    if is_bottom_right(y, x):
        count += 1
    if is_top_right(y, x):
        count += 1
    if is_bottom_left(y, x):
        count += 1
    if is_convex_top_left(y, x):
        count += 1
    if is_convex_bottom_right(y, x):
        count += 1
    if is_convex_top_right(y, x):
        count += 1
    if is_convex_bottom_left(y, x):
        count += 1
    return count

#region Test corner_count
def set_tile(data:list, y:int, x:int, value:str):
    if y < 0 or y >= len(data) or x < 0 or x >= len(data[y]):
        return
    data[y] = data[y][:x] + value + data[y][x+1:]

def print_data(data:list):
    for d in data:
        print(d)

marker = []
for y in range(len(data)):
    marker.append(data[y])

for y in range(len(data)):
    for x in range(len(data[y])):
        c = corner_count(y, x)
        if c != 0:
            set_tile(marker, y, x, str(c))
      
print_data(marker)

#endregion

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
    s = corner_count(y, x)
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
