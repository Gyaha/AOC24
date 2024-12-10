data = '2333133121414131402'

with open('Input/09.txt') as f:
    data = f.read().strip()
    pass

data = [int(x) for x in data]

# is file (True, length, id)
# is space (False, length)


class File():
    def __init__(self, is_file, length, id=None):
        self.is_file = is_file
        self.length = length
        self.id = id

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        if self.is_file:
            return f'File({self.length}, {self.id})'
        else:
            return f'Space({self.length})'


print('Creating filesystem index')

filesystem = []
is_file = False
file_id = -1
for i in range(len(data)):
    current_data = data[i]
    is_file = not is_file
    if is_file:
        file_id += 1
        filesystem.append(File(is_file=True, length=current_data, id=file_id))
    else:
        filesystem.append(File(is_file=False, length=current_data))

# print(filesystem)


def try_to_fit(file_index: int, filesystem: list) -> int:
    file = filesystem[file_index]
    if file.is_file == False:
        return None
    for i in range(len(filesystem)):
        if i == file_index:
            break
        target = filesystem[i]
        if target.is_file == False and target.length >= file.length:
            return i
    return None


def fit_file(file_index: int, space_index: int, filesystem: list):
    file = filesystem.pop(file_index)
    filesystem.insert(file_index, File(is_file=False, length=file.length))
    space = filesystem.pop(space_index)
    space.length -= file.length
    if space.length > 0:
        filesystem.insert(space_index, space)
    filesystem.insert(space_index, file)


print('Fitting files into spaces')

i = len(filesystem) - 1
while i > 0:
    t = try_to_fit(i, filesystem)
    if t != None:
        fit_file(i, t, filesystem)
        i += 1
    else:
        i -= 1

print('Writing filesystem')

filesystem_list = []

for f in filesystem:
    if f.is_file:
        for i in range(f.length):
            filesystem_list.append(f.id)
    else:
        for i in range(f.length):
            filesystem_list.append(0)

total = 0
for i in range(len(filesystem_list)):
    current_data = filesystem_list[i]
    total += current_data * i

print(total)
