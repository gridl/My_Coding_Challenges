import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = (lines.rstrip())
        if line:
            line = line.split(',')
            s = line[0]
            if line[1] in s:
                print (len(s) - 1) - s[::-1].find(line[1])
            else:
                print '-1'
#reverse string: s[::-1] or 'string'[::-1]
