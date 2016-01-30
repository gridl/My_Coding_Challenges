import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        x, y, n = lines.rstrip().split(' ')
        x, y, n = int(x), int(y), int(n)
        for i in range(1,n+1):
            if i % x == 0 and i % y == 0:
                print 'FB',
            elif i % x == 0:
                print 'F',
            elif i % y == 0:
                print 'B',
            else:
                print i,
        print ''
