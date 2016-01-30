import sys


with open(sys.argv[1], 'r') as f:
    for lines in f:
        res = []
        for i in lines.rstrip().split(','):
            if i.find('.') < i.find('Y'):
                res.append(i.count('.'))
            else:
                res.append(0)
        print min(res)
