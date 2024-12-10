import re

data = 'xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))'
data = 'xmul(2,4)&mul[3,7]!^don\'t()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))'
# with open("Input/03.txt") as f:
#    data = f.read()

# print(re.findall('mul\(([0-9]+),([0-9]+)\)', data))


def sum_text(text):
    t = 0
    for match in re.finditer('mul\(([0-9]+),([0-9]+)\)', data):
        a, b = map(int, match.groups())
        t += a * b
    return t


data = 'do()' + data + 'don\'t()'
# print(data)
t = 0
for match in re.findall('do\(\)(.*)don\'t\(\)', data):
    print('asdf')
    print(match)


# TODO FIX THIS
asdf
