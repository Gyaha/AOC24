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


def is_all_connected(group):
    for computer_a in group:
        for computer_b in group:
            if computer_a == computer_b:
                continue
            if computer_b not in connections[computer_a]:
                return False
    return True


def find_groups(computer):
    group = [computer]
    for connection in connections[computer]:
        if is_all_connected(group + [connection]):
            group.append(connection)
    return group


groups = []
for computer in computers:
    group = find_groups(computer)
    group.sort()
    if group not in groups:
        groups.append(group)
        # print(group)

groups.sort(key=lambda x: len(x), reverse=True)
print(",".join(groups[0]))
