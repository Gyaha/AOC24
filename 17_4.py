# Maybe reverse engineering the program is the way to go?!
# Sure does not seem like it.
# Well it did speed it up by ~3x

# But I did see that the output is 'slow' in the end

program = [2, 4,  # b = a % 8
           1, 1,  # b = b ^ 1
           7, 5,  # c = a // (2 ^ b)
           0, 3,  # a = a // pow(2, 3)
           4, 7,  # b = b ^ c
           1, 6,  # b = b ^ 6
           5, 5,  # out = b % 8
           3, 0]  # if a == 0: break

cache = {}


def rec_run(a):
    if a in cache:
        return cache[a]
    initial_a = a
    b = a % 8
    b = b ^ 1
    c = a // pow(2, b)
    a = a // pow(2, 3)
    b = b ^ c
    b = b ^ 6
    out = [b % 8]
    if a != 0:
        out += rec_run(a)
    cache[initial_a] = out
    return out


# Find the first number that matches the length of the program

a = 0
move_by = 0
while True:
    moved_by = pow(2, move_by)
    print(a, '->', a + moved_by)
    a += moved_by
    out = rec_run(a)
    if len(out) == len(program):
        if move_by == 0:
            break
        a -= moved_by
        print(a, '<-', a + moved_by)
        move_by = 0
    else:
        move_by += 1

print(a)


def find_lowest_where(a, action):
    b = 0
    move_by = 0
    while True:
        moved_by = pow(2, move_by)
        print(b, '->', b + moved_by)
        b += moved_by
        out = rec_run(a + b)
        if action(out):
            if move_by == 0:
                break
            b -= moved_by
            print(b, '<-', b + moved_by)
            move_by = 0
        else:
            move_by += 1
    return b


a_0 = find_lowest_where(0, lambda x: len(x) == len(program))
a_0_output = rec_run(a)

a_1 = find_lowest_where(a_0, lambda x: x[len(x)-1] != a_0_output[len(a_0_output)-1])
a_2 = find_lowest_where(a_0, lambda x: x[len(x)-2] != a_0_output[len(a_0_output)-2])
a_3 = find_lowest_where(a_0, lambda x: x[len(x)-3] != a_0_output[len(a_0_output)-3])
a_4 = find_lowest_where(a_0, lambda x: x[len(x)-4] != a_0_output[len(a_0_output)-4])
a_5 = find_lowest_where(a_0, lambda x: x[len(x)-5] != a_0_output[len(a_0_output)-5])
a_6 = find_lowest_where(a_0, lambda x: x[len(x)-6] != a_0_output[len(a_0_output)-6])
a_7 = find_lowest_where(a_0, lambda x: x[len(x)-7] != a_0_output[len(a_0_output)-7])
a_8 = find_lowest_where(a_0, lambda x: x[len(x)-8] != a_0_output[len(a_0_output)-8])

print(a_0)
print(a_1)
print(a_2)
print(a_3)
print(a_4)
print(a_5)
print(a_6)
print(a_7)
print(a_8)

print(find_lowest_where(0, lambda x: len(x) == len(program)-3))
