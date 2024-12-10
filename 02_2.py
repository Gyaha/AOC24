data = """7 6 4 2 1
1 2 7 8 9
9 7 6 2 1
1 3 2 4 5
8 6 4 4 1
1 3 6 7 9""".splitlines()

with open("Input/02.txt") as f:
    data = f.read().splitlines()

data = [[int(x) for x in line.split()] for line in data]


def check_report(line):
    past_reading = line[0]
    direction = line[0] > line[1]
    for i in range(1, len(line)):
        next_reading = line[i]
        # print(past_reading, next_reading)
        if past_reading > next_reading:
            if not direction:
                # print('- Wrong direction')
                return False
            distance = past_reading - next_reading
        elif past_reading < next_reading:
            if direction:
                # print('- Wrong direction')
                return False
            distance = next_reading - past_reading
        else:
            # print('- No movement')
            return False
        if distance > 3:
            # print('- Distance too great:', distance)
            return False
        past_reading = next_reading
    # print('---')
    return True


def check_report_twice(line):
    if check_report(line):
        return True
    for i in range(len(line)):
        line_copy = line.copy()
        line_copy.pop(i)
        if check_report(line_copy):
            return True


t = 0
for line in data:
    if check_report_twice(line):
        t += 1

print(t)
