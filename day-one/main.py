import sys

try:
    with open('input.txt') as file:
        list = [ int(line) for line in file ]
except Exception as e:
    print(repr(e))
    sys.exit()

for x in list:
    for y in list:
        for z in list:
            if x != y and y != z and x + y + z == 2020:
                print("{} + {} + {} = 2020".format(x, y, z))
                print("{} * {} * {} = {}".format(x, y, z, x * y * z))
                sys.exit()