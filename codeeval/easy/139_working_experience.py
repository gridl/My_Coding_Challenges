import sys
import datetime

months = {
    'Jan': 0,
    'Feb': 1,
    'Mar': 2,
    'Apr': 3,
    'May': 4,
    'Jun': 5,
    'Jul': 6,
    'Aug': 7,
    'Sep': 8,
    'Oct': 9,
    'Nov': 10,
    'Dec': 11
}

with open(sys.argv[1], 'r') as f:
    for lines in f:
        total = {i: [0 for _ in xrange(12)] for i in xrange(1990, 2021)}
        line = (lines.rstrip()).split('; ')
        times = [i.split('-') for i in line]
        res = []
        for i in times:
            res.append((i[0].split(),i[1].split()))
        for k in res:
            start_m, start_y = months[k[0][0]], int(k[0][1])
            end_m, end_y = months[k[1][0]], int(k[1][1])
            for year in xrange(start_y,end_y+1):
                if year == start_y:
                    start = start_m
                else:
                    start = 0
                if year == end_y:
                    end = end_m + 1
                else:
                    end = 12
                for mon in xrange(start,end):
                    total[year][mon] = 1
        exp = sum(sum(p for p in total[i] if p == 1) for i in total.keys())
        print exp/12

