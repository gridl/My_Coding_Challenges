import sys
import re

reg = re.compile(r"(.+?)\1+")

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip()
        list = re.findall(reg,line)
        if list:
            print len(list[0])
        else:
            print len(line)
