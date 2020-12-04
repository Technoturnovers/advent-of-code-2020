import sys

def read_file(path: str) -> str:
    try:
        with open(path) as file:
            return file.read()
    except Exception as e:
        print(repr(e))
        sys.exit()

def part_one(blob: str) -> int:
    entries = blob.split('\n\n')
    counter = 0
    required = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    for entry in entries:
        if all(substr in entry for substr in required):
            counter += 1
    return counter

if __name__ == '__main__':
    blob = read_file('day-four/input.txt')
    print(part_one(blob))