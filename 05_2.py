rules = []
pages = []

with open('Input/input05.txt') as f:
    data = f.readlines()

data_test = """47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47""".splitlines()

# data = data_test

for line in data:
    if '|' in line:
        # (str, str)
        rules.append(line.strip().split('|'))
    elif ',' in line:
        # (str, str, ...)
        pages.append(line.strip().split(','))
    else:
        pass


def try_rule_on_page(rule, page):
    if rule[0] not in page or rule[1] not in page:
        return True
    return page.index(rule[0]) < page.index(rule[1])


def is_page_valid(rules, page):
    for rule in rules:
        if not try_rule_on_page(rule, page):
            return False
    return True


def solve_page(rules, page):
    while (not is_page_valid(rules, page)):
        for rule in rules:
            if not try_rule_on_page(rule, page):
                # Swap the page indexes
                i = page.index(rule[0])
                j = page.index(rule[1])
                page[i], page[j] = page[j], page[i]
    return page


t = 0
for page in pages:
    if not is_page_valid(rules, page):
        page = solve_page(rules, page)
        t += int(page[(len(page)//2)])

print(t)
