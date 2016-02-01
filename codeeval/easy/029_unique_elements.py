import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = (lines.rstrip()).split(',')
        last = 0
        uni = []
        for i in line:
            if i == last:
                continue
            else:
                last = i
                uni.append(i)
        print ','.join(uni)
