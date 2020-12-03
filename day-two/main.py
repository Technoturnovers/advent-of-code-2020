import re
import sys

try:
    with open('input.txt') as file:
        list = [ line for line in file ]
except Exception as e:
    print(repr(e))
    sys.exit()

counta = 0
countb = 0

for entry in list:
    bounds = re.findall('[0-9]+', entry)
    lower = int(bounds[0])
    upper = int(bounds[1])
    alphas = re.findall('[a-z]+', entry)
    char = alphas[0]
    passwd = alphas[1]
    if lower <= passwd.count(char) and passwd.count(char) <= upper:
        counta += 1
    if (passwd[lower - 1] == char or passwd[upper - 1] == char) and not(passwd[lower - 1] == char and passwd[upper - 1] == char):
        countb += 1

print(counta)
print(countb)