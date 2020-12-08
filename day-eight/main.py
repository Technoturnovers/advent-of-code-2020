import sys

def read_file(path: str) -> list:
    try:
        with open(path) as file:
            return [line.strip() for line in file]
    except Exception as e:
        print(repr(e))
        sys.exit()

# My reference implementation of the syntax, no
# special behavior
def reference(prg: list) -> int:
    acc = 0
    pos = 0
    while pos <= len(prg) - 1:
        cur = prg[pos]
        if cur.startswith('nop'):
            pass
        elif cur.startswith('acc'):
            acc += int(cur[4:])
        elif cur.startswith('jmp'):
            pos += int(cur[4:])
            continue
        pos += 1
    return acc

def part_one(prg: list) -> int:
    acc = 0
    pos = 0
    already_ran = []
    while pos <= len(prg) - 1:
        if pos in already_ran:
            return acc
        else:
            already_ran.append(pos)
        cur = prg[pos]
        if cur.startswith('nop'):
            pass
        elif cur.startswith('acc'):
            acc += int(cur[4:])
        elif cur.startswith('jmp'):
            pos += int(cur[4:])
            continue
        pos += 1
    return acc

def part_two(prg: list) -> int:
    for idx, instruction in enumerate(prg):
        copy = prg.copy()
        good = True
        if copy[idx].startswith('acc'):
            continue
        elif copy[idx].startswith('jmp'):
            copy[idx] = instruction.replace('jmp', 'nop')
        elif copy[idx].startswith('nop'):
            copy[idx] = instruction.replace('nop', 'jmp')
        print(instruction + " " + copy[idx])
        pos = 0
        acc = 0
        already_ran = []
        while pos <= len(copy) - 1:
            if pos in already_ran:
                good = False
                break
            else:
                already_ran.append(pos)
            cur = copy[pos]
            if cur.startswith('nop'):
                pass
            elif cur.startswith('acc'):
                acc += int(cur[4:])
            elif cur.startswith('jmp'):
                pos += int(cur[4:])
                continue
            pos += 1
        if good:
            return acc

if __name__ == '__main__':
    prg = read_file('day-eight/input.txt')
    # print(part_one(prg))
    print(part_two(prg))