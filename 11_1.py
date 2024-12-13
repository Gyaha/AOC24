# I will try and use two lists and iterration append to solve this problem

data = '125 17'
with open('Input/11.txt', 'r') as file:
    data = file.read()

data = [int(x) for x in data.split()]

def run(data):
    new_data = []
    for d in data:
        if d == 0:
            new_data.append(1)
            continue
        d_str = str(d)
        if(len(d_str) % 2 == 0):
            half = len(d_str) // 2
            first_half = d_str[:half]
            second_half = d_str[half:]
            new_data.append(int(first_half))
            new_data.append(int(second_half))
            continue
        new_data.append(d * 2024)
    return new_data

for i in range(25):
    data = run(data)

print(len(data))