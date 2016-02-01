import sys

sum = 0

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip()
        sum += int(line)

print sum
