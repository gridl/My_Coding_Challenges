import sys


with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = (lines.rstrip()).split(' ')
        res = [False for _ in xrange(len(line))]
        cur = ''
        for n,i in enumerate(line):
            if i != cur:
                pos = n
                cur = i
                res.insert(pos,[cur])
            elif i == cur:
                res[pos] = res[pos] + [i]
        res2 = []
        for j in res:
            if j:
                res2.append(str(len(j)))
                res2.append(str(j[0]))
        print ' '.join(res2)
