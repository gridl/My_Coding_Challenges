import sys
import datetime

with open(sys.argv[1], 'r') as f:
    for lines in f:
        num = int(lines.rstrip())
        res = ''
        if num / 1000:
            res += str(num/1000 * 'M')
            num = num - (num/1000)*1000
        if num / 100:
            if num / 100 <4:
                res += str('C' * (num/100))
            elif num /100 == 4:
                res += str('CD')
            elif num / 100 == 5:
                res += str('D')
            elif num / 100 > 5 and num / 100 < 9:
                res += str('D' + 'C'*(num/100 - 5))
            elif num / 100 == 9:
                res += str('CM')
            num = num -(num/100) * 100
        if num / 10:
            if num / 10 <4:
                res += str('X' * (num/10))
            elif num /10 == 4:
                res += str('XL')
            elif num / 10 == 5:
                res += str('L')
            elif num / 10 > 5 and num / 10 < 9:
                res += str('L' + 'X'*(num/10 - 5))
            elif num / 10 == 9:
                res += str('XC')
            num = num -(num/10) * 10
        if num / 1:
            if num / 1 <4:
                res += str('I' * (num/1))
            elif num /1 == 4:
                res += str('IV')
            elif num / 1 == 5:
                res += str('V')
            elif num / 1 > 5 and num / 1 < 9:
                res += str('V' + 'I'*(num/1-5))
            elif num / 1 == 9:
                res += str('IX')
        print res
