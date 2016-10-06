L = [ '1 8', '2 4' ]

for i in L:

    zeros, nulls = i.split()
    bin_list = [ bin(int(num))[2:] for num in range(1, int(nulls)+1) ]
    result = [ j for j in bin_list if j.count('0') == int(zeros) ]

    print len(result)
