import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        words = lines.rstrip().split(' ')
        print words[-2]
