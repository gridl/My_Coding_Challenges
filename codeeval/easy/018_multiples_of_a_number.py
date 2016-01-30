import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        x, n = lines.rstrip().split(',')
        x, n = int(x), int(n)
        for i in range(1,x):
            if n * i >= x:
                n *= i
                break
        print n
