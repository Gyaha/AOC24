# Well this does do the thing...
# But it would take way to long to run.


from itertools import permutations

data = """x00: 0
x01: 1
x02: 0
x03: 1
x04: 0
x05: 1
y00: 0
y01: 0
y02: 1
y03: 1
y04: 0
y05: 1

x00 AND y00 -> z05
x01 AND y01 -> z02
x02 AND y02 -> z01
x03 AND y03 -> z03
x04 AND y04 -> z04
x05 AND y05 -> z00"""

# with open('Input/24.txt', 'r') as file:
#    data = file.read()

data = data.split('\n')

# (type, data_1, data_2)

original_gates = {}

for line in data:
    if ':' in line:
        id, value = line.split(': ')
        original_gates[id] = ('literal', int(value), None)
    elif '->' in line:
        value, id = line.split(' -> ')
        if ' AND ' in value:
            a, b = value.split(' AND ')
            original_gates[id] = ('and', a, b)
        elif ' OR ' in value:
            a, b = value.split(' OR ')
            original_gates[id] = ('or', a, b)
        elif ' XOR ' in value:
            a, b = value.split(' XOR ')
            original_gates[id] = ('xor', a, b)


def translate_gate(key, gates):
    type, a, b = gates[key]
    if type == 'literal':
        return a
    elif type == 'and':
        if translate_gate(a, gates) == 1 and translate_gate(b, gates) == 1:
            return 1
        else:
            return 0
    elif type == 'or':
        if translate_gate(a, gates) == 1 or translate_gate(b, gates) == 1:
            return 1
        else:
            return 0
    elif type == 'xor':
        if translate_gate(a, gates) != translate_gate(b, gates):
            return 1
        else:
            return 0
    else:
        return 'error'


def keys_to_numbers(keys, gates):
    b = '0b'
    for key in keys:
        b += str(translate_gate(key, gates))
    return int(b, base=0)


def number_to_keys(number, keys, gates):
    b = bin(number)[2:]
    b = '0' * (len(keys) - len(b)) + b
    for i, key in enumerate(keys):
        gates[key] = ('literal', int(b[i]), None)


def swap_gates(gates, a, b):
    key_a = gates[a]
    key_b = gates[b]
    # print('Swapping', a, key_a, 'and', b, key_b)
    gates[a] = key_b
    gates[b] = key_a


def set_inputs(gates, x, y):
    x_gates = [key for key in gates if key.startswith('x')]
    x_gates.sort(reverse=True)
    number_to_keys(x, x_gates, gates)
    y_gates = [key for key in gates if key.startswith('y')]
    y_gates.sort(reverse=True)
    number_to_keys(y, y_gates, gates)


def try_tests(original_gates, swaps, x, y):
    gates = original_gates.copy()

    set_inputs(gates, x, y)

    for a, b in swaps:
        swap_gates(gates, a, b)

    x_gates = [key for key in gates if key.startswith('x')]
    x_gates.sort(reverse=True)
    number_1 = keys_to_numbers(x_gates, gates)

    y_gates = [key for key in gates if key.startswith('y')]
    y_gates.sort(reverse=True)
    number_2 = keys_to_numbers(y_gates, gates)

    z_gates = [key for key in gates if key.startswith('z')]
    z_gates.sort(reverse=True)
    number_3 = keys_to_numbers(z_gates, gates)

    # print(number_1, '+', number_2, '=', number_3)
    return number_1 + number_2 == number_3


def try_swaps(original_gates, swaps):
    gates = original_gates.copy()

    for a, b in swaps:
        swap_gates(gates, a, b)

    x_gates = [key for key in gates if key.startswith('x')]
    x_gates.sort(reverse=True)
    number_1 = keys_to_numbers(x_gates, gates)

    y_gates = [key for key in gates if key.startswith('y')]
    y_gates.sort(reverse=True)
    number_2 = keys_to_numbers(y_gates, gates)

    z_gates = [key for key in gates if key.startswith('z')]
    z_gates.sort(reverse=True)
    number_3 = keys_to_numbers(z_gates, gates)

    # print(number_1, '+', number_2, '=', number_3)
    return number_1 + number_2 == number_3


all_gates = list(original_gates.keys())

i = 0
for p in permutations(all_gates, 8):
    i += 1
    if i % 10000 == 0:
        print(sorted(p))
    try:
        swaps = [(p[0], p[1]), (p[2], p[3]), (p[4], p[5]), (p[6], p[7])]
        if try_swaps(original_gates, swaps):
            if try_tests(original_gates, swaps, 10, 20) and try_tests(original_gates, swaps, 20, 10) and try_tests(original_gates, swaps, 12, 21) and try_tests(original_gates, swaps, 21, 12):
                print('Works')
                print(','.join(sorted(p)))
                break
            else:
                pass
    except:
        pass


quit()
