import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip()[:-1].split('; ')
        dist = sorted([int(i.split(',')[1]) for i in line])
        res =[]
        for j,d in enumerate(dist):
            if j == 0:
               res.append(dist[j])
            else:
                res.append(dist[j] - dist[j-1])
        print ','.join(str(n) for n in res)
