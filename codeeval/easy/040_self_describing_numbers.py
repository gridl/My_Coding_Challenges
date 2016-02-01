import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        l = line.rstrip()
        k = 0
        for i,n in enumerate(l):
            if int(n) == l.count(str(i)):
                k +=1
        if k == len(l):
            print 1
        else:
            print 0
