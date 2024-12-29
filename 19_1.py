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

#print(designs)
#print(possibilities)

cache = {}

def rec_check_possibility(possibility, pointer=0):
    if possibility[pointer:] in cache:
        return cache[possibility[pointer:]]
    if len(possibility) == pointer:
        return True
    for design in designs:
        if design == possibility[pointer:pointer+len(design)]:
            if rec_check_possibility(possibility, pointer+len(design)):
                cache[possibility[pointer:]] = True
                return True
    cache[possibility[pointer:]] = False
    return False
    
t = 0
for possibility in possibilities:
    #print(f"Checking possibility: {possibility}")
    if rec_check_possibility(possibility):
        t += 1
        #print("Found possibility")
print(t)