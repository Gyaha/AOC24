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


d = Door(original_wires)
d.set_wires(['x00', 'x01', 'x02', 'x03', 'x04', 'x05'], number_to_input(10, 6))
d.set_wires(['y00', 'y01', 'y02', 'y03', 'y04', 'y05'], number_to_input(2, 6))
print(output_to_number(d.get_wires(['z00', 'z01', 'z02', 'z03', 'z04', 'z05'])))
