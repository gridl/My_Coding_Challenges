import sys

#http://www.rapidtables.com/convert/number/degrees-to-degrees-minutes-seconds.htm

with open(sys.argv[1], 'r') as f:
    for line in f:
        angle = float(line.rstrip())
        whole = int(angle)
        min = int((angle - whole) * 60)
        sec = int((angle - whole - float(min)/60)*3600)
        print '''%d.%02d'%02d"''' % (whole,min,sec)
