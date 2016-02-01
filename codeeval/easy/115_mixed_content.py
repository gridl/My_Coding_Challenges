import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip().split(',')
        words = [i for i in line if i.isalpha()]
        digits = [i for i in line if i.isdigit()]
        if words and digits:
            w = ','.join(words)
            d = ','.join(digits)
            print str(w)+'|'+str(d)
        elif words:
            print ','.join(words)
        else:
            print ','.join(digits)
