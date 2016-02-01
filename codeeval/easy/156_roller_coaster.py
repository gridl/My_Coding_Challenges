import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = list(lines.rstrip())
        i = 0
        for n,l in enumerate(line):
            if l.isalpha():
                if i%2 == 0:
                    i += 1
                    line[n] = l.upper()
                elif i%2 == 1:
                    i += 1
        print ''.join(line)
