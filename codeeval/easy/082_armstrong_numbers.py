import sys

with open(sys.argv[1], 'r') as f:
    for line in f:
        l = line.rstrip()
        length = len(l)
        number = int(l)
        sum = 0
        for i in l:
            sum += pow(int(i), length)
        if number == sum:
            print True
        else:
            print False
