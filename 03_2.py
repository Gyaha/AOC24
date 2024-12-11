import re

data = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'

with open("Input/03.txt") as f:
    data = f.read()


def sum_text(text):
    t = 0
    for match in re.finditer(r'mul\(([0-9]+),([0-9]+)\)', text):
        a,b = int(match.group(1)), int(match.group(2))
        t += a * b
    return t


data = data.replace('\n', '')
data = 'do()' + data + 'don\'t()'

t = 0
for match in re.finditer(r'do\(\)(.*?)don\'t\(\)', data):
    t += sum_text(str(match.group(1)))

print(t)