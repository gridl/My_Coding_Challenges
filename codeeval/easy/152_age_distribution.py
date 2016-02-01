import sys

with open(sys.argv[1], 'r') as f:
    for lines in f:
        line = int(lines.rstrip())
        if line in range(0,3):
            print "Still in Mama's arms"
        elif line in range(3,5):
            print 'Preschool Maniac'
        elif line in range(5,12):
            print 'Elementary school'
        elif line in range(12,15):
            print 'Middle school'
        elif line in range(15,19):
            print 'High school'
        elif line in range(19,23):
            print 'College'
        elif line in range(23,66):
            print 'Working for the man'
        elif line in range(66,101):
            print 'The Golden Years'
        else:
            print "This program is for humans"
