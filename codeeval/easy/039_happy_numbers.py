import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        num = int(lines.rstrip())
        while True:
            if num == 1:
                print '1'
                break
            if num == 4:
                print '0'
                break
            num = sum(int(i) ** 2 for i in str(num))
