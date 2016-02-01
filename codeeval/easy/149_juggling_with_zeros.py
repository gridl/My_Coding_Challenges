import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = (lines.rstrip()).split(' ')
        flags = [i for i in line[::2]]
        values = [j for j in line[1::2]]
        res = ''
        for f,n in zip(flags,values):
            if f == '00':
                res += '1'* len(n)
            elif f == '0':
                res += n
        print int(res,2)
