data = '2333133121414131402'

with open('Input/09.txt') as f:
    data = f.read().strip()

data = [int(x) for x in data]

filesystem = []
is_file = False
file_id = -1
for i in range(len(data)):
    current_data = data[i]
    is_file = not is_file
    if is_file:
        file_id += 1
        for j in range(current_data):
            filesystem.append(file_id)
    else:
        for j in range(current_data):
            filesystem.append(None)

# print(filesystem)

for i in range(len(filesystem)):
    if i >= len(filesystem):
        break
    if filesystem[i] == None:
        f = None
        while f == None:
            f = filesystem.pop()
        filesystem[i] = f

# print(filesystem)

total = 0
for i in range(len(filesystem)):
    current_data = filesystem[i]
    total += current_data * i

print(total)
