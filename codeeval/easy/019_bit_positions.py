import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip().split(',')
        number, p1, p2 = line
        number, p1, p2 = int(number), int(p1), int(p2)

        binar = str(bin(number))[2:]
        if binar[-p1] == binar[-p2]:
            print 'true'
        else:
            print 'false'
