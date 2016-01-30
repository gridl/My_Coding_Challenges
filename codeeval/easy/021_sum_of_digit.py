import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        di = [int(i) for i in lines.rstrip()]
        print sum(di)
