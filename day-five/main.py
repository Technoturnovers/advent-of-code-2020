import sys

def read_file(path: str) -> list:
    try:
        with open(path) as file:
            return [line.strip() for line in file]
    except Exception as e:
        print(repr(e))
        sys.exit()

def part_one(bpasses: list) -> list:
    taken = []
    for bpass in bpasses:
        bpass = bpass.replace('B', '1')
        bpass = bpass.replace('F', '0')
        bpass = bpass.replace('R', '1')
        bpass = bpass.replace('L', '0')
        buffer = int(bpass[:-3], 2) * 8 + int(bpass[-3:], 2)
        taken.append(buffer)
    return taken

def part_two(bpasses: list) -> int:
    for i in range(min(bpasses), max(bpasses)):
        if i not in bpasses and i - 1 in bpasses and i + 1 in bpasses:
            return i

if __name__ == '__main__':
    bpasses = read_file('day-five/input.txt')
    taken = part_one(bpasses)
    print(max(taken))
    print(part_two(taken))