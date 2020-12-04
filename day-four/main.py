import re
import sys

def read_file(path: str) -> str:
    try:
        with open(path) as file:
            return file.read()
    except Exception as e:
        print(repr(e))
        sys.exit()

def part_one(blob: str) -> list:
    entries = blob.split('\n\n')
    valid = []
    required = ['byr:', 'iyr:', 'eyr:', 'hgt:', 'hcl:', 'ecl:', 'pid:']
    for entry in entries:
        if all(substr in entry for substr in required):
            valid.append(entry.strip())
    return valid

def part_two(entries: list) -> list:
    counter = 0
    entries = [{field.split(':')[0]:field.split(':')[1] for field
               in entry.split()} for entry in entries]
    valid = []
    for entry in entries:
        if not 1920 <= int(entry['byr']) <= 2002:
            continue
        if not 2010 <= int(entry['iyr']) <= 2020:
            continue
        if not 2020 <= int(entry['eyr']) <= 2030:
            continue
        if entry['hgt'].endswith('cm'):
            if not 150 <= int(entry['hgt'][:-2]) <= 193:
                continue
        if entry['hgt'].endswith('in'):
            if not 59 <= int(entry['hgt'][:-2]) <= 76:
                continue
        if not re.match(r'#[a-f0-9]{6}', entry['hcl']):
            continue
        hair_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
        if not any(substr in entry['ecl'] for substr in hair_colors):
            continue
        if not re.match(r'\d{9}', entry['pid']):
            continue
        print(entry)
        valid.append(entry)
    return valid


if __name__ == '__main__':
    blob = read_file('day-four/input.txt')
    valid = part_one(blob)
    print(len(valid))
    valid = part_two(valid)
    print(len(valid))