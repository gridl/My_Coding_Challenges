import sys
import time

def sec(time):
    t = time.split(':')
    return int(t[0]) * 3600 + int(t[1]) * 60 + int(t[2])

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = (lines.rstrip()).split(' ')
        d1 = sec(line[0])
        d2 = sec(line[1])
        if d1 >= d2:
            print time.strftime('%H:%M:%S', time.gmtime(d1-d2))
        elif d2 > d1:
            print time.strftime('%H:%M:%S', time.gmtime(d2-d1))
