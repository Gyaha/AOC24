from itertools import combinations, permutations, product
import sys
sys.setrecursionlimit(100)

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

with open('Input/24.txt', 'r') as file:
    data = file.read()


data = data.split('\n')

# (type, data_1, data_2)
original_wires = {}

# Parse the data
for line in data:
    if ':' in line:
        id, value = line.split(': ')
        original_wires[id] = ('literal', int(value), None)
    elif '->' in line:
        value, id = line.split(' -> ')
        if ' AND ' in value:
            a, b = value.split(' AND ')
            original_wires[id] = ('and', a, b)
        elif ' OR ' in value:
            a, b = value.split(' OR ')
            original_wires[id] = ('or', a, b)
        elif ' XOR ' in value:
            a, b = value.split(' XOR ')
            original_wires[id] = ('xor', a, b)


class Door():
    def __init__(self, wires):
        self.x = None
        self.y = None
        self.z = None
        self.wires = wires

    def swap_wires(self, wire_a, wire_b):
        if self.wires[wire_a][0] == 'literal' or self.wires[wire_b][0] == 'literal':
            raise Exception('Cannot swap literals')
        self.wires[wire_a], self.wires[wire_b] = self.wires[wire_b], self.wires[wire_a]

    def set_wire(self, wire, value):
        if self.wires[wire][0] != 'literal':
            raise Exception('Cannot set non-literals')
        self.wires[wire] = ('literal', value, None)

    def set_wires(self, wires, values):
        if len(wires) != len(values):
            raise Exception('Length mismatch')
        for wire, value in zip(wires, values):
            self.set_wire(wire, value)

    def get_wire(self, wire):
        type, a, b = self.wires[wire]
        if type == 'literal':
            return a
        elif type == 'and':
            if self.get_wire(a) == 1 and self.get_wire(b) == 1:
                return 1
            else:
                return 0
        elif type == 'or':
            if self.get_wire(a) == 1 or self.get_wire(b) == 1:
                return 1
            else:
                return 0
        elif type == 'xor':
            if self.get_wire(a) != self.get_wire(b):
                return 1
            else:
                return 0
        else:
            raise Exception('Error')

    def get_wires(self, wires):
        return [self.get_wire(wire) for wire in wires]


def output_to_number(b: list):
    # Takes a list of 1s and 0s and returns the number
    b = ''.join(map(str, b))
    return int(b, base=2)


def number_to_input(n: int, length: int):
    # Takes a number and returns a list of 1s and 0s
    b = bin(n)[2:]
    if len(b) > length:
        raise Exception(f'Number is too long: {n} ({b}) ({length})')
    b = b.zfill(length)
    return list(map(int, b))


def get_wires_starting_with(wires, start):
    return sorted([w for w in wires if w.startswith(start)])


def wire_number(xyz, number):
    return xyz + str(number).zfill(2)


def test_wire(number, door):
    # Can't test wire 0
    if number == 0:
        return True

    x_wire_prev = wire_number('x', number - 1)
    y_wire_prev = wire_number('y', number - 1)

    x_wire = wire_number('x', number)
    y_wire = wire_number('y', number)

    z_wire = wire_number('z', number)

    z_wire_next = wire_number('z', number + 1)

    # First test the x and y wires
    door.set_wire(x_wire, 0)
    door.set_wire(y_wire, 0)
    if door.get_wire(z_wire) != 0:
        return False
    if door.get_wire(z_wire_next) != 0:
        return False

    door.set_wire(x_wire, 1)
    door.set_wire(y_wire, 0)
    if door.get_wire(z_wire) != 1:
        return False
    if door.get_wire(z_wire_next) != 0:
        return False

    door.set_wire(x_wire, 0)
    door.set_wire(y_wire, 1)
    if door.get_wire(z_wire) != 1:
        return False
    if door.get_wire(z_wire_next) != 0:
        return False

    door.set_wire(x_wire, 1)
    door.set_wire(y_wire, 1)
    if door.get_wire(z_wire) != 0:
        return False
    if door.get_wire(z_wire_next) != 1:
        return False

    door.set_wire(x_wire, 0)
    door.set_wire(y_wire, 0)

    # Now test previous xy wires
    door.set_wire(x_wire_prev, 0)
    door.set_wire(y_wire_prev, 0)
    if door.get_wire(z_wire) != 0:
        return False

    door.set_wire(x_wire_prev, 1)
    door.set_wire(y_wire_prev, 0)
    if door.get_wire(z_wire) != 0:
        return False

    door.set_wire(x_wire_prev, 0)
    door.set_wire(y_wire_prev, 1)
    if door.get_wire(z_wire) != 0:
        return False

    door.set_wire(x_wire_prev, 1)
    door.set_wire(y_wire_prev, 1)
    if door.get_wire(z_wire) != 1:
        return False

    door.set_wire(x_wire_prev, 0)
    door.set_wire(y_wire_prev, 0)


door = Door(original_wires)

all_wires = list(original_wires.keys())
x_wires = get_wires_starting_with(original_wires, 'x')
y_wires = get_wires_starting_with(original_wires, 'y')
z_wires = get_wires_starting_with(original_wires, 'z')
all_non_xy_wires = [w for w in all_wires if w not in x_wires and w not in y_wires]


door.set_wires(x_wires, number_to_input(0, len(x_wires)))
door.set_wires(y_wires, number_to_input(0, len(y_wires)))

for i in range(len(x_wires)):
    door.set_wires(x_wires, number_to_input(0, len(x_wires)))
    door.set_wires(y_wires, number_to_input(0, len(y_wires)))
    if test_wire(i, door) is False:
        print(f'Failed test for wire {i}')
