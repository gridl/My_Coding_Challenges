import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = ''.join(lines.rstrip().split(' '))
        min = []
        for i in set(line):
            if line.count(i) == 1:
                min.append(i)
        if not min:
            print 0
        else:
            print line.find(sorted(min)[0]) + 1
