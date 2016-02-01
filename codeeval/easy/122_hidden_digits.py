import sys
import string

di = {j:i for i,j in enumerate(string.ascii_lowercase[:10])}

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip()
        res_line = []
        for i in line:
            if i.isdigit():
                res_line.append(i)
            elif i in di.keys():
                res_line.append(str(di[i]))
        if res_line:
            print ''.join(res_line)
        else:
            print 'NONE'
