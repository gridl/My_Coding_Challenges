import sys
import json


with open(sys.argv[1], 'r') as f:
    for lines in f:
        dict = json.loads(lines.rstrip())
        l = dict["menu"]["items"]
        label_sum = 0
        for i in l:
            if i:
                if 'label' in i:
                    label_sum += int(i['id'])
        print label_sum
