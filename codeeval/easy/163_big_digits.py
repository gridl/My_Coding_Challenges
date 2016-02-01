import sys

string = """-**----*--***--***---*---****--**--****--**---**--
*--*--**-----*----*-*--*-*----*-------*-*--*-*--*-
*--*---*---**---**--****-***--***----*---**---***-
*--*---*--*-------*----*----*-*--*--*---*--*----*-
-**---***-****-***-----*-***---**---*----**---**--
--------------------------------------------------"""

sss = string.split('\n')
numbers = []

numbers = [[k[j*5:j*5+5] for k in sss] for j in range(10)]

with open(sys.argv[1], 'r') as f:
    for line in f:
        res = [int(i) for i in line.rstrip() if i.isdigit()]
        for m in range(6):
            str_f = ''
            for num in res:
                str_f += str(numbers[num][m])
            print str_f
