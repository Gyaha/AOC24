data = """#####
.####
.####
.####
.#.#.
.#...
.....

#####
##.##
.#.##
...##
...#.
...#.
.....

.....
#....
#....
#...#
#.#.#
#.###
#####

.....
.....
#.#..
###..
###.#
###.#
#####

.....
.....
.....
#....
#.#..
#.#.#
#####"""

with open("Input/25.txt") as f:
    data = f.read()


data = data.strip().split("\n\n")


keys = []
locks = []


def pin_counter(pins):
    rows = [0 for _ in range(len(pins[0]))]
    for y in range(len(pins)):
        for x in range(len(pins[y])):
            if pins[y][x] == "#":
                rows[x] += 1
    return rows


for d in data:
    d = d.splitlines()
    if d[0][0] == "#":
        locks.append(pin_counter(d[1:-1]))
    else:
        keys.append(pin_counter(d[1:-1]))


print(keys)
print(locks)
print()


def key_fits(key, lock):
    for i in range(len(key)):
        if (key[i] + lock[i]) > 5:
            return False
    return True


fits = 0
for lock in locks:
    # print('Lock:', lock)
    for key in keys:
        # print('Key:', key)
        if key_fits(key, lock):
            # print('Fits')
            fits += 1
print(fits)
