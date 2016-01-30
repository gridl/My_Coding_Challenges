import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip().split(' ')
        print ' '.join(line[::-1])
