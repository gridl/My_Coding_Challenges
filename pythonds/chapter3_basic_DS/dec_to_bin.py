from stack_implementation import Stack

def decimal_to_bin(number):
    s = Stack()

    while number > 0:
        s.push( number % 2 )
        number //= 2

    bin_str = ''
    while not s.isEmpty():
        bin_str += str(s.pop())

    return bin_str


def convert_to_base(number, base):
    convert = '0123456789ABCDEF'

    s = Stack()

    while number > 0:
        s.push( convert[number % base] )
        number //= base

    result = ''
    while not s.isEmpty():
        result += str(s.pop())

    return result



if __name__ == "__main__":
    print( decimal_to_bin(5) )
    print( decimal_to_bin(4) )

    print( convert_to_base(25, 2) )
    print( convert_to_base(25, 16) )
