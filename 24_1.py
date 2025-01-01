data = """x00: 1
x01: 0
x02: 1
x03: 1
x04: 0
y00: 1
y01: 1
y02: 1
y03: 1
y04: 1

ntg XOR fgs -> mjb
y02 OR x01 -> tnw
kwq OR kpj -> z05
x00 OR x03 -> fst
tgd XOR rvg -> z01
vdt OR tnw -> bfw
bfw AND frj -> z10
ffh OR nrd -> bqk
y00 AND y03 -> djm
y03 OR y00 -> psh
bqk OR frj -> z08
tnw OR fst -> frj
gnj AND tgd -> z11
bfw XOR mjb -> z00
x03 OR x00 -> vdt
gnj AND wpb -> z02
x04 AND y00 -> kjc
djm OR pbm -> qhw
nrd AND vdt -> hwm
kjc AND fst -> rvg
y04 OR y02 -> fgs
y01 AND x02 -> pbm
ntg OR kjc -> kwq
psh XOR fgs -> tgd
qhw XOR tgd -> z09
pbm OR djm -> kpj
x03 XOR y03 -> ffh
x00 XOR y04 -> ntg
bfw OR bqk -> z06
nrd XOR fgs -> wpb
frj XOR qhw -> z04
bqk OR frj -> z07
y03 OR x01 -> nrd
hwm AND bqk -> z03
tgd XOR rvg -> z12
tnw OR pbm -> gnj"""

with open('Input/24.txt', 'r') as file:
    data = file.read()

data = data.split('\n')

# (type, data_1, data_2)

gates = {}

for line in data:
    if ':' in line:
        id, value = line.split(': ')
        gates[id] = ('literal', int(value), None)
    elif '->' in line:
        value, id = line.split(' -> ')
        if ' AND ' in value:
            a, b = value.split(' AND ')
            gates[id] = ('and', a, b)
        elif ' OR ' in value:
            a, b = value.split(' OR ')
            gates[id] = ('or', a, b)
        elif ' XOR ' in value:
            a, b = value.split(' XOR ')
            gates[id] = ('xor', a, b)

gates_starting_with_z = [key for key in gates if key.startswith('z')]
gates_starting_with_z.sort(reverse=True)


def translate_gate(key):
    type, a, b = gates[key]
    if type == 'literal':
        return a
    elif type == 'and':
        if translate_gate(a) == 1 and translate_gate(b) == 1:
            return 1
        else:
            return 0
    elif type == 'or':
        if translate_gate(a) == 1 or translate_gate(b) == 1:
            return 1
        else:
            return 0
    elif type == 'xor':
        if translate_gate(a) != translate_gate(b):
            return 1
        else:
            return 0
    else:
        return 'error'


t = '0b'
for key in gates_starting_with_z:
    t += str(translate_gate(key))
print(int(t, base=0))
