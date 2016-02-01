import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line, key  = lines.rstrip().split(';')
        line = line.split(' ')
        key = [int(k) for k in key.split(' ')]
        key += (set([j for j in xrange(1,len(key)+1)]) - set(key))
        sentence = line[:]
        for i in key:
            sentence[int(i)-1] = line[key.index(i)]
        print ' '.join(sentence)

