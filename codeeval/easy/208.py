import sys

with open(sys.argv[1]) as f:
    for line in f:
        table = [ row.split() for row in line.split('|') ]

        category_table = [ [ int(row[i]) for row in table ] for i in range(len(table[0])) ]

        print ' '.join([ str(i) for i in map(max, category_table)])
