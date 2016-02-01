import sys

numb = {'zero':0, 'one':1, 'two':2, 'three':3, 'four':4, 'five':5, 'six':6, 'seven':7, 'eight':8, 'nine':9}

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = (lines.rstrip()).split(';')
        numbers = []
        for i in line:
            numbers.append(str(numb[i]))
        print ''.join(numbers)
