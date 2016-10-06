import sys


with open(sys.argv[1]) as f:
    for line in f:
        words = line.strip().split()
        result = []
        for word in words:
            word = list(word)
            word[0], word[-1] = word[-1], word[0]
            result.append(''.join(word))
        print ' '.join(result)


