import sys


with open(sys.argv[1]) as f:
    for line in f:
        nums, iterations = line.strip().split(' | ')
        nums = [int(n) for n in nums.split()]
        iterations = int(iterations)

        for i in range(iterations):
            pos = 0
            first = nums[pos]
            second = nums[pos+1]
            while not first > second:
                pos += 1
                first = nums[pos]
                second = nums[pos+1]

            nums[pos] = second
            nums[pos+1] = first
        print ' '.join([str(j) for j in nums])

