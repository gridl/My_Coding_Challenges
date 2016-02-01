import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = (lines.rstrip()).split(' ')
        numb = [float(i) for i in line]
        res = [i for i in sorted(numb)]
        for n in res:
            print '%.3f' % n,
        print ''
