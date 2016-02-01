import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip().split(',')
        major = [i for i in set(line) if line.count(i) > len(line)/2]
        if major:
            print major[0]
        else:
            print 'None'
