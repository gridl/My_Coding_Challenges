import sys

with open(sys.argv[1]) as f:
    for line in f:
        virus, antivirus = line.strip().split('|')
        virus_sum = sum([int(i, 16) for i in virus.split()])
        antivirus_sum = sum([int(i, 2) for i in antivirus.split()])
        print(antivirus_sum >= virus_sum)
