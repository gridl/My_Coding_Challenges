import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip()
        letters = ''
        for i in line:
            if i.isalpha():
                letters += i.lower()
        L = []
        for i in set(letters):
            L.append(letters.count(i))
        L = list(reversed(sorted(L)))
        sum = 0
        for num,i in enumerate(reversed(range(27-len(L),27))):
            sum += L[num] * i
        print sum
