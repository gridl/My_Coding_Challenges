import sys

def split(number,symb,line):
    pos = line.find(symb)
    num1 = int(number[:pos])
    num2 = int(number[pos:])
    if symb == '+':
        return num1 + num2
    elif symb == '-':
        return num1 - num2

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = lines.rstrip().split(' ')
        num = line[0]
        if '-' in line[1]:
            print split(num,'-',line[1])
        elif '+' in line[1]:
            print split(num,'+',line[1])
