import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip()
        if len(line) <= 55:
            print line
        elif len(line) > 55:
            line = line[:40]
            if ' ' in line:
                line = line[:(len(line) - line[::-1].find(' ') - 1)]
            print line + '... <Read More>'
