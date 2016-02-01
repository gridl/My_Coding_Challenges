import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = (lines.rstrip()).split(' : ')
        numbers = line[0].split(' ')
        swap = line[1].split(', ')
        for i in swap:
            sw = i.split('-')
            a = numbers[int(sw[0])]
            b = numbers[int(sw[1])]
            numbers[int(sw[0])] = b
            numbers[int(sw[1])] = a
        print ' '.join(numbers)
