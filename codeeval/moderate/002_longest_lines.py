import sys

with open(sys.argv[1], 'r') as f:
    lines = [line.rstrip() for line in f]

    line_num = int(lines[0])
    dict_len_lines = {len(i):i for i in lines[1:]}
    sorted_len = sorted(dict_len_lines,reverse=True)

    for n in range(line_num):
        print dict_len_lines[sorted_len[n]]
