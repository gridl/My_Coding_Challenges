import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        n,m = (lines.rstrip()).split(',')
        n = int(n)
        m = int(m)
        print (n - ((n/m) * m))
