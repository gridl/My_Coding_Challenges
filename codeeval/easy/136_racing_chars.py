import sys


with open(sys.argv[1], 'r') as f:
    road = [lines.rstrip() for lines in f]

def repl(sym,line,prev_place):
    cur_place = line.find(sym)
    if cur_place < prev_place:
        line = line.replace(sym,'/')
    elif cur_place > prev_place:
        line = line.replace(sym,'\\')
    else:
        line = line.replace(sym,'|')
    prev_place = cur_place
    road[n] = line
    return prev_place


for n,l in enumerate(road):
    if n == 0:
        if 'C' in l:
            l = l.replace('C','|')
            prev_place = l.find('C')
        elif '_' in l:
            prev_place = l.find('_')
            l = l.replace('_','|')
        road[n] = l
    elif 'C' in l:
        prev_place = repl('C',l,prev_place)
    elif '_' in l:
        prev_place = repl('_',l,prev_place)
for i in road:
    print i
