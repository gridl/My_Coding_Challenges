import sys


with open(sys.argv[1]) as f:
    for line in f:
        nums = ''.join(line.strip().split())
        thirds = sum([ int(i)*2 for i in nums[::2]])
        other = sum([ int(i) for i in nums[1::2]])
        result = thirds + other
        if str(result).endswith('0'):
            print('Real')
        else:
            print('Fake')
