from stack_implementation import Stack
import string
import operator

def infix_to_postfix(infix_exp):
    operators = Stack()
    infix_exp = infix_exp.split()
    precedence = { '^': 4,
                   '*': 3,
                   '/': 3,
                   '+': 2,
                   '-': 2,
                   '(': 1 }

    postfix = []
    for sym in infix_exp:
        if sym in string.ascii_letters or sym.isdigit():
            postfix.append(sym)
        elif sym == '(':
            operators.push(sym)
        elif sym == ')':
            while not operators.peek() == '(':
                postfix.append( operators.pop() )
            operators.pop()
        elif sym in precedence.keys():
            while not operators.isEmpty() and precedence[operators.peek()] >= precedence[sym]:
                postfix.append(operators.pop())
            operators.push(sym)
        else:
            raise TypeError("Wrong expression")
    while not operators.isEmpty():
        postfix.append(operators.pop())
    return ' '.join(postfix)


def eval_postfix(postfix_exp):
    operands = Stack()
    postfix = postfix_exp.split()
    operators = { '*': operator.mul,
                  '/': operator.truediv,
                  '+': operator.add,
                  '-': operator.sub,
                  '^': operator.pow }

    for sym in postfix:
        if sym.isdigit():
            operands.push(int(sym))
        elif sym in operators.keys():
            second = operands.pop()
            first = operands.pop()
            operands.push( operators[sym](first, second) )
        else:
            raise TypeError("Wrong expression")
    return operands.pop()


if __name__ == "__main__":
    print("Convert infix to postfix:")
    print("A * B + C * D", '\t\t', infix_to_postfix("A * B + C * D"))
    print('( A + B ) * C - ( D - E ) * ( F + G )', '\t\t',
          infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))

    print("Eval postfix: ")
    print(eval_postfix('17 8 + 3 2 + /'))
    print(eval_postfix('5 3 4 2 - ^ *'))
