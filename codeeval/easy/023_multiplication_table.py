for i in xrange(1,13):
    for j in xrange(1,13):
        m = i*j
        if j == 1:
            print m,
        else:
            print '%3d' % m,
    print '\n',
