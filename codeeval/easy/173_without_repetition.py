import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip()
        res = []
        for i,char in enumerate(line):
            if i == 0:
                res.append(char)
            elif char == line[i-1]:
                pass
            else:
                res.append(char)
        print ''.join(res)
