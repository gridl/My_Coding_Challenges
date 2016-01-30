import sys

slangd = {
    0 : ', yeah!',
    1 : ', this is crazy, I tell ya.',
    2 : ', can U believe this?',
    3 : ', eh?',
    4 : ', aw yea.',
    5 : ', yo.',
    6 : '? No way!',
    7 : '. Awesome!',
}


punct = ['.', '!', '?']

yes = 0
slang_count = 0

with open(sys.argv[1], 'r') as f:
    for lines in f:
        res = []
        for char in lines.rstrip():
            if char not in punct:
                res.append(char)
            elif char in punct and yes == 0:
                yes += 1
                res.append(char)
                pass
            elif char in punct and yes == 1:
                res.append(slangd[slang_count%8])
                slang_count += 1
                yes -= 1
        print ''.join(res)

