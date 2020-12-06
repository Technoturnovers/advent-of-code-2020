import re
import string
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
    count = 0
    for entry in entries:
        for letter in string.ascii_lowercase:
            if letter in entry:
                count += 1
    return count
    
def part_two(blob: str) -> int:
    groups = [ group.split() for group in blob.split('\n\n') ]
    count = 0
    for group in groups:
        for letter in string.ascii_lowercase:
            if all(letter in entry for entry in group):
                count += 1
    return count
    
if __name__ == '__main__':
    blob = read_file('day-six/input.txt')
    print(part_one(blob))
    print(part_two(blob))