import string
import re
alphabet = string.ascii_lowercase


def contains_straight(w):
    for i in xrange(len(w) - 2):
        if alphabet.index(w[i]) + 2 == alphabet.index(w[i + 1]) + 1 == alphabet.index(w[i + 2]):
            return True
    return False


def no_bad_chars(w):
    return re.match('.*[iol].*', w) is None


def has_pairs(w):
    pair1 = re.match('.*(([a-z])\\2{1}).*', w)
    if pair1:
        letter = pair1.groups()[1]
        return re.match('.*(([a-z])\\2{1}).*', w.replace(letter, ' ')) is not None
    return False


def valid(w):
    return no_bad_chars(w) and has_pairs(w) and contains_straight(w)


def increment_pw(pw):
    i = len(pw) - 1
    while i >= 0 and pw[i] == 'z':
        i -= 1
    chars = list(pw)
    chars[i] = alphabet[alphabet.index(chars[i]) + 1]
    for i in xrange(i + 1, len(pw)):
        chars[i] = 'a'
    return ''.join(chars)


def next_password(pw):
    pw = increment_pw(pw)
    while True:
        if valid(pw):
            break
        pw = increment_pw(pw)
    return pw

pw = next_password('vzbxkghb')
print 'part 1', pw
print 'part 2', next_password(pw)
