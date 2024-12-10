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

left.sort()
right.sort()
right.reverse()

t = 0
for i in range(len(left)):
    a, b = left[i], right[len(left)-i-1]
    d = 0
    if a > b:
        d = a - b
    else:
        d = b - a
    t += d
    print(a, b, d)

print(t)
