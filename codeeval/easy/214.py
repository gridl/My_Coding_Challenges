import sys

with open(sys.argv[1]) as f:
    for line in f:
        result = sorted(line.strip().split(), reverse=True)
        print ' '.join(result)
