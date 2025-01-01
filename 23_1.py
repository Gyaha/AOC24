data = """kh-tc
qp-kh
de-cg
ka-co
yn-aq
qp-ub
cg-tb
vc-aq
tb-ka
wh-tc
yn-cg
kh-ub
ta-co
de-co
tc-td
tb-wq
wh-td
ta-ka
td-qp
aq-cg
wq-ub
ub-vc
de-ta
wq-aq
wq-vc
wh-yn
ka-de
kh-ta
co-tc
wh-qp
tb-vc
td-yn"""

with open('Input/23.txt', 'r') as file:
    data = file.read()

data = data.strip().split('\n')

computers = set()
connections = {}

for line in data:
    a, b = line.split('-')
    if a not in connections:
        connections[a] = set()
    if b not in connections:
        connections[b] = set()
    connections[a].add(b)
    connections[b].add(a)
    computers.add(a)
    computers.add(b)

# print(connections)
# print(computers)

groups = []

for computer_a in computers:
    for computer_b in connections[computer_a]:
        for computer_c in connections[computer_a]:
            if computer_b == computer_c:
                continue
            if computer_c in connections[computer_b]:
                # This was smart to sort the group to test if it's already in the list
                group = [computer_a, computer_b, computer_c]
                group.sort()
                if group not in groups:
                    groups.append(group)

total = 0
for group in groups:
    for computer in group:
        if computer[0] == 't':
            total += 1
            break
print(total)
