import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip().split(' | ')
        list1 = line[0].split(' ')
        list2 = line[1].split(' ')
        lists = zip(list1,list2)
        res = []
        for i,j in lists:
            res.append(str(int(i)*int(j)))
        print ' '.join(res)
