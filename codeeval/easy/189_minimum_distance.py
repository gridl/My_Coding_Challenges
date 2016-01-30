import sys


with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip().split()
        friends = sorted([int(i) for i in line[1:]])
        fin = []
        for i in friends:
            mid = i
            fin.append(sum([abs(j - mid) for j in friends]))
        print min(fin)
