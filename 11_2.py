# Yeah, knew this would happen
# TBH, I am not sure this is doable in python

data = '125 17'
with open('Input/11.txt', 'r') as file:
    data = file.read()

data = data.strip()

def run_n(number:str):
    if number == '0':
        return '1', None
    if len(number) % 2 == 0:
        half = len(number) // 2
        return number[:half], str(int(number[half:]))
    return str(int(number) * 2024), None

cache_rec = {}
def rec_run(data:str, left:int):
    cache_id = (data, left)
    if cache_id in cache_rec:
        return cache_rec[cache_id]
    if left == 0:
        return 1
    a, b = run_n(data)
    if b is None:
        val = rec_run(a, left-1)
        cache_rec[cache_id] = val
        return val
    val = rec_run(a, left-1) + rec_run(b, left-1)
    cache_rec[cache_id] = val
    return val
    
total = 0
for d in data.split(' '):
    total += rec_run(d, 75)
print(total)
