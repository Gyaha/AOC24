data = """r, wr, b, g, bwu, rb, gb, br

brwrr
bggr
gbbr
rrbgbr
ubwu
bwurrg
brgr
bbrgwb"""

with open("Input/19.txt", "r") as f:
    data = f.read()

designs, possibilities = data.split("\n\n")

designs = designs.strip().split(", ")
possibilities = possibilities.strip().split("\n")

# print(designs)
# print(possibilities)

check_cache = {}


def rec_check_possibility(possibility, pointer=0):
    if possibility[pointer:] in check_cache:
        return check_cache[possibility[pointer:]]
    if len(possibility) == pointer:
        return True
    for design in designs:
        if design == possibility[pointer:pointer+len(design)]:
            if rec_check_possibility(possibility, pointer+len(design)):
                check_cache[possibility[pointer:]] = True
                return True
    check_cache[possibility[pointer:]] = False
    return False


count_cache = {}


def rec_count_possibility(possibility, pointer=0):
    # Holy **** this is fast
    if possibility[pointer:] in count_cache:
        return count_cache[possibility[pointer:]]
    if len(possibility) == pointer:
        return 1
    count = 0
    for design in designs:
        if design == possibility[pointer:pointer+len(design)]:
            count += rec_count_possibility(possibility, pointer+len(design))
    count_cache[possibility[pointer:]] = count
    return count


t = 0
for possibility in possibilities:
    # print(f"Checking possibility: {possibility}")
    if rec_check_possibility(possibility):
        t += rec_count_possibility(possibility)
        # print("Found possibility")
print(t)
