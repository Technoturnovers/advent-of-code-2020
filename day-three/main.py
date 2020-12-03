import sys

def input(path: str) -> list:
    try:
        with open(path) as file:
            return [ line.rstrip() for line in file ]
    except Exception as e:
        print(repr(e))

def partone(map: list) -> int:
    count = 0
    x = 0
    x_slope = 3
    y = 0
    y_slope = 1
    while y < len(map) - 1:
        x += x_slope
        y += y_slope
        if map[y][x % len(map[y])] == '#':
            count += 1
    return count

if __name__ == "__main__":
    map = input('input.txt')
    print(partone(map))