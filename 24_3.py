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


def get_wires_starting_with(wires, start):
    return sorted([w for w in wires if w.startswith(start)], reverse=True)


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


door = Door(original_wires)

x_wires = get_wires_starting_with(original_wires, 'x')
y_wires = get_wires_starting_with(original_wires, 'y')
z_wires = get_wires_starting_with(original_wires, 'z')

for i in range(len(x_wires)):
    door.set_wires(x_wires, number_to_input(0, len(x_wires)))
    door.set_wires(y_wires, number_to_input(0, len(y_wires)))
    for j in range(2):
        x_wire = x_wires[i]
        y_wire = y_wires[i]
        z_wire = z_wires[i]
        door.set_wire(x_wire, j)
        door.set_wire(y_wire, j)
        print(door.get_wire(z_wire))
    print()

quit()

for i in range(4):
    for j in range(4):
        k = i + j
        # print(i, j, k)
        print()
        print(i, bin(i)[2:].zfill(3))
        print(j, bin(j)[2:].zfill(3))
        print(k, bin(k)[2:].zfill(3))
