L = [ "(--9Hello----World...--)", "Can 0$9 ---you~", "13What213are;11you-123+138doing7" ]

import sys

with open(sys.argv[1], 'r') as f:
    for curr_str in f:
        result = ''
        last_alpha = False
        for sym in curr_str:
            if sym.isalpha():
                result += sym.lower()
                last_alpha = True
            else:
                if last_alpha:
                    result += ' '
                    last_alpha = False
        print result
