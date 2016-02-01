import sys

with open(sys.argv[1], 'r') as f:
    for numbers in f:
        number = numbers.rstrip()
        print int(number, 16)

