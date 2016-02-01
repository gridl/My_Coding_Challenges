import sys

with open(sys.argv[1], 'r') as f:
    for num in f:
        number = int(num.rstrip())
        if number % 2 == 0:
            print 1
        else:
            print 0
