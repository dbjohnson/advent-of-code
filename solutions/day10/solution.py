def look_and_say(x):
    c = x[0]
    n = 1
    expanded = ''
    for cc in x[1:]:
        if cc != c:
            expanded += '{}{}'.format(n, c)
            c = cc
            n = 0
        n += 1
    expanded += '{}{}'.format(n, c)
    return expanded


for part, repeat in (('part 1', 40), ('part 2', 50)):
    x = '1113122113'
    for _ in xrange(repeat):
        x = look_and_say(x)
    print part, len(x)
