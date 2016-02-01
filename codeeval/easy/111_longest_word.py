import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        words = lines.rstrip().split(' ')
        length = sorted({len(w) for w in words},reverse=True)
        for word in words:
            if len(word) == length[0]:
                print word
                break
            else:
                pass
