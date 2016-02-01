import sys
import math

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = (lines.rstrip()).split(') (')
        x1,y1 = ((line[0])[1:]).split(', ')
        x2,y2 = ((line[1])[:-1]).split(', ')
        line_len = int(math.sqrt((int(x2)-int(x1))**2 + (int(y2)-int(y1))**2))
        print line_len
