import sys
from math import sqrt

with open(sys.argv[1], 'r') as f:
    for lines in f:
        num = int(lines.rstrip())
        print int(((1+sqrt(5))**num-(1-sqrt(5))**num)/(2**num*sqrt(5)))
