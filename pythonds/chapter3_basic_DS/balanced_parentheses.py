from stack_implementation import Stack

def check_parentheses(expression):
    """

    """
    s = Stack()
    for symbol in expression:
        if symbol == '(':
            s.push(symbol)
        elif symbol == ')':
            if s.isEmpty():
                return False
            else:
                s.pop()
    if s.isEmpty():
        return True
    else:
        return False


def general_parentheses_checker(expression):

    sym_dict = {')':'(', '}': '{', ']': '['}

    s = Stack()
    for symbol in expression:
        if symbol in '([{':
            s.push(symbol)
        elif symbol in ')]}':
            if s.isEmpty():
                return False
            else:
                if sym_dict[symbol] == s.peek():
                    s.pop()
                else:
                    return False
    if s.isEmpty():
        return True
    else:
        return False


if __name__ == '__main__':
    print( check_parentheses('((()))') )
    print( check_parentheses('(()') )
    print( general_parentheses_checker('{{([][])}()}'))
    print( general_parentheses_checker('[{()]'))
