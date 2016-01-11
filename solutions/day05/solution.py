import re


with open('input.txt', 'r') as fh:
    lines = [l.strip() for l in fh.readlines()]

vowels = 'aeiou'
bad = ['ab', 'cd', 'pq', 'xy']


def nice(word):
    vowel_count = sum(word.count(v) for v in vowels) >= 3
    double = re.match('.*(([a-z])\\2{1}).*', word) is not None
    no_bads = not any(b in word for b in bad)
    return all([vowel_count, double, no_bads])


print 'part 1', len(filter(nice, lines))


def nice_pt2(word):
    repeat_pair = re.match('.*([a-z]{2}).*\\1.*', word) is not None
    repeat_letter = re.match('.*([a-z])[a-z]\\1.*', word) is not None
    return repeat_pair and repeat_letter


print 'part 2', len(filter(nice_pt2, lines))


