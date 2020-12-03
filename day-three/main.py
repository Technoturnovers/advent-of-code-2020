import sys

def input(path: str) -> list:
    try:
        with open(path) as file:
            return [ line.rstrip() for line in file ]
    except Exception as e:
        print(repr(e))
        sys.exit()

def trees(map: list, x_slope: int, y_slope: int) -> int:
    count = 0
    x = 0
    y = 0
    while y < len(map) - 1:
        x += x_slope
        y += y_slope
        if map[y][x % len(map[y])] == '#':
            count += 1
    return count

def part_two(map: list) -> int:
    product = 1
    slopes = [ (1, 1), (3, 1), (5, 1), (7, 1), (1, 2) ]
    for pair in slopes:
        product *= trees(map, pair[0], pair[1])
    return product

if __name__ == "__main__":
    map = input('day-three/input.txt')
    print(trees(map, 3, 1)) # Part One
    print(part_two(map)) # Part Two