import sys


with open(sys.argv[1]) as f:
    for line in f:
        if line.split():
            teams = line.strip().split(' | ')
            d_countries = { n: t.split() for n, t in enumerate(teams, 1) }

            unique_teams = []
            for v in d_countries.values():
                unique_teams += v
            unique_teams = sorted(list(set([int(i) for i in unique_teams])))
            result = ''
            for team in unique_teams:
                countries = [ country for country, c_teams in d_countries.items() if str(team) in c_teams ]
                result += str(team)+':'+','.join([str(i) for i in sorted(countries)])+'; '
            result = result.rstrip()
            print result


