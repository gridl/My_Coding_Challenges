import sys

matrix = [[0 for n in xrange(256)] for n in xrange(256)]

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip().split(' ')
        cmd = line[0]
        if cmd == 'SetRow':
            i = int(line[1])
            x = int(line[2])
            for k in xrange(256):
                matrix[i][k] = x
        elif cmd == 'SetCol':
            j = int(line[1])
            x = int(line[2])
            for row in matrix:
                row[j] = x
        elif cmd == 'QueryRow':
            i = int(line[1])
            print sum(matrix[i])
        elif cmd == 'QueryCol':
            j = int(line[1])
            print sum([n[j] for n in matrix])
