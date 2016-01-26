import re


def look_and_say(x):
    return ''.join('{}{}'.format(len(c.group()), c.group()[0])
                   for c in re.finditer('([0-9])\\1*', x))

for part, repeat in (('part 1', 40), ('part 2', 50)):
    x = '1113122113'
    for _ in xrange(repeat):
        x = look_and_say(x)
    print part, len(x)
