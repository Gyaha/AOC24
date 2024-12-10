data = """3   4
4   3
2   5
1   3
3   9
3   3""".splitlines()

with open("Input/01.txt") as f:
    data = f.read().splitlines()

left, right = [], []
for line in data:
    a, b = map(int, line.split())
    left.append(a)
    right.append(b)


t = 0
for i in range(len(left)):
    v = left[i]
    t += right.count(v) * v

print(t)
