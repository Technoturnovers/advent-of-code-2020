import re
import sys

def read_file(path: str) -> dict:
    bags = {}
    try:
        with open(path) as file:
            for line in file:
                contents = []
                matches = re.findall(r'(\d )?(\w+ \w+ bag)', line)
                if ''.join(matches[1]) == 'no other bag':
                    continue
                for bag in matches[1:]:
                    contents += [''.join(bag)[2:]] * int(''.join(bag)[0])
                bags.update({''.join(matches[0]): contents})
            return bags
    except Exception as e:
        print(repr(e))
        sys.exit()

def part_one(rules: dict) -> int:
    copy = rules.copy()
    copy.pop('shiny gold bag')
    lookfor = ['shiny gold bag']
    working = True
    while working:
        buffer = lookfor.copy()
        for bag, contents in copy.items():
            if any(a in contents for a in lookfor) and bag not in buffer:
                buffer.append(bag)
        if buffer == lookfor:
            working = False
        lookfor = buffer.copy()
    return len(lookfor) - 1

def part_two(rules: dict, bag: str) -> int:
    count = 0
    for item in rules[bag]:
        if item in rules.keys():
            count += part_two(rules, item) + 1
        else:
            count += 1
    return count

if __name__ == '__main__':
    rules = read_file('day-seven/input.txt')
    print(part_one(rules))
    print(part_two(rules, 'shiny gold bag'))