import sys


with open(sys.argv[1]) as f:
    for line in f:
        words = line.strip().split()
        max_length = max([ len(w) for w in words ])
        max_words = [ word for word in words if len(word) == max_length ]
        result = []
        for pos, letter in enumerate(max_words[0]):
            result.append(pos*'*' + letter)

        print ' '.join(result)

