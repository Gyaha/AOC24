data = """1
10
100
2024"""

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


def run_x_times(secret, x):
    for _ in range(x):
        secret = run(secret)
    return secret


# region test run_x_times()
assert run_x_times(1, 2000) == 8685429
assert run_x_times(10, 2000) == 4700978
assert run_x_times(100, 2000) == 15273692
assert run_x_times(2024, 2000) == 8667524
# endregion

run_x = 2000


def run_input(data):
    result = 0
    for secret in data:
        result += run_x_times(secret, run_x)
    return result


print(run_input(data))
