data = """1
2
3
2024"""

test_pattern = [-2, 1, -1, 3]

with open("Input/22.txt", "r") as file:
    data = file.read()

data = data.strip().split("\n")
data = [int(x) for x in data]


def mix(value, secret):
    return value ^ secret


def prune(secret):
    return secret % 16777216


# region test mix & prune
assert mix(15, 42) == 37
assert prune(100000000) == 16113920
# endregion


def run(secret):
    # Calculate the result of multiplying the secret number by 64.
    # Then, mix this result into the secret number.
    # Finally, prune the secret number.
    secret = prune(mix(secret * 64, secret))
    # Calculate the result of dividing the secret number by 32.
    # Round the result down to the nearest integer.
    # Then, mix this result into the secret number.
    # Finally, prune the secret number.
    secret = prune(mix(secret // 32, secret))
    # Calculate the result of multiplying the secret number by 2048.
    # Then, mix this result into the secret number.
    # Finally, prune the secret number.
    secret = prune(mix(secret * 2048, secret))

    return secret


# region test run()
expected = [
    15887950,
    16495136,
    527345,
    704524,
    1553684,
    12683156,
    11100544,
    12249484,
    7753432,
    5908254
]
result = 123
for i in range(10):
    result = run(result)
    if result != expected[i]:
        print(f"Error: {i}")
# endregion

TIMES_TO_RUN = 2000

price_lists = []
price_stats = []


def secret_to_price(secret):
    return int(str(secret)[-1])


def get_price_list(secret):
    prices = [secret_to_price(secret)]
    for _ in range(TIMES_TO_RUN):
        secret = run(secret)
        prices.append(secret_to_price(secret))
    return prices


for secret in data:
    price_lists.append(get_price_list(secret))

for i in range(len(price_lists)):
    price_stats.append([])
    for j in range(len(price_lists[i])):
        if j == 0:
            price_stats[i].append(0)
            continue
        prev = price_lists[i][j - 1]
        price_stats[i].append(price_lists[i][j] - prev)

# print(price_lists[0][0:10])
# print(price_stats[0][0:10])

pattern_values = {}

for i in range(len(price_stats)):
    price_stat = price_stats[i]
    price_list = price_lists[i]
    seen_patterns = set()
    for j in range(len(price_stat) - 3):
        pattern = tuple(price_stat[j:j+4])
        if pattern in seen_patterns:
            continue
        seen_patterns.add(pattern)
        if pattern not in pattern_values:
            pattern_values[pattern] = 0
        pattern_values[pattern] += price_list[j+3]


pattern_values = sorted(pattern_values.items(), key=lambda x: x[1], reverse=True)
print(pattern_values[0][1])
