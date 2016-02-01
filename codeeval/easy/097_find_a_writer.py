import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip()
        letters = (line.split('|'))[0]
        keys = ((line.split('| '))[1]).split(' ')
        writer = []
        for i in keys:
            writer.append(letters[(int(i)-1)])
        print ''.join(writer)
