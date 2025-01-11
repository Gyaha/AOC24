# Maybe reverse engineering the program is the way to go?!
# Sure does not seem like it.
# Well it did speed it up by ~3x

# But I did see that the output is 'slow' in the end

# Well it works now, check the cache_fix() and iter_fix_index() for more info.

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
    # Run the program on a simple function
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


def find_lowest_where(a, action):
    # Find the first number that (ACTION) is True
    b = 0
    move_by = 0
    while True:
        moved_by = pow(2, move_by)
        # print(b, '->', b + moved_by)
        b += moved_by
        out = rec_run(a + b)
        if action(out):
            if move_by == 0:
                break
            b -= moved_by
            # print(b, '<-', b + moved_by)
            move_by = 0
        else:
            move_by += 1
    return b


# region Cache Fix
# This is the number added to change the output at that index.
# This is first found by finding the lowest number that changes the output at that index.
# But then I saw a pattern and just set that to the cache_fix.
# Basically pow(2,(index + 3)).
# Then divide by 1024 to make it skip less numbers.
# This is NOT perfect, but it works.
cache_fix = {}
zero = find_lowest_where(0, lambda x: len(x) == len(program))
zero_output = rec_run(zero)
result = zero
for i in range(1, len(program)+1):
    index = len(zero_output)-i
    # print('i:', index)
    cache_fix[index] = find_lowest_where(zero, lambda x: x[index] != zero_output[index])
# print(cache_fix)

d = 0
for i in range(1, 47, 3):
    # print(d, '\t', cache_fix[d])
    # print(i, '\t', pow(2, i))
    cache_fix[d] = pow(2, i) // 1024
    d += 1
cache_fix[0] = 1
cache_fix[1] = 1
cache_fix[2] = 1
# endregion


def iter_fix_index(a, program=program):
    # Travels from back to front and tries to match the output and program.
    # If it does not match, it adds the cache_fix to the number.
    # Then it checks from the start again.
    last_index = len(program)-1
    index = last_index
    while rec_run(a) != program:
        b = cache_fix[index]
        # print(rec_run(a))
        if rec_run(a)[index] != program[index]:
            a += b
            print(rec_run(a))
            index = last_index
            continue
        if index == 0:
            return a
        index -= 1
    return a


zero = find_lowest_where(0, lambda x: len(x) == len(program))
result = iter_fix_index(zero, program)
print()
print(rec_run(result))
print(program)
print(result)
