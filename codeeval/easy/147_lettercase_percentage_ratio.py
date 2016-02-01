import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        lower = 0
        upper = 0
        line = lines.rstrip()
        for i in line:
            if i.islower():
                lower += 1
            elif i.isupper():
                upper += 1
        print 'lowercase: %.2f uppercase: %.2f' % ((float(lower)/len(line))*100,(float(upper)/len(line))*100)
