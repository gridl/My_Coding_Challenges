import sys

words = []
with open(sys.argv[1], 'r') as f:
    for line in f:
        words.extend(line.split(' '))

for word in words:
    print word.swapcase(),
