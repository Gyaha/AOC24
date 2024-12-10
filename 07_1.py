data = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20""".splitlines()

with open('Input/07.txt') as f:
    data = f.read().splitlines()


def calc(target, values, current_sum=0):
    if len(values) == 0:
        return target == current_sum
    c = 0
    c += calc(target, values[1:], current_sum + values[0])
    c += calc(target, values[1:], current_sum * values[0])
    return c


t = 0
for line in data:
    target, values = line.split(': ')
    target = int(target)
    values = list(map(int, values.split(' ')))
    if calc(target, values):
        t += target
print(t)
