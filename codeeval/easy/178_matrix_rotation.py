import sys
from math import sqrt

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip().split(' ')
        size = int(sqrt(len(line)))
        matrix = [line[i*size:i*size+size] for i in xrange(size)]
        rotate = [[matrix[j][i] for j in xrange(size)] for i in xrange(size)]
        res = []
        for i in rotate:
            res.extend(i[::-1])
        print ' '.join(res)
