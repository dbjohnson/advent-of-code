def fibonacci(i):
    # can't do "classic" recursive fibonacci here - i is too large
    s = 1
    for c in xrange(i):
        s += c + 1
    return s


def row_col_to_idx(row, col):
    row -= 1
    col -= 1
    return fibonacci(row + col) + col


target_row = 2981
target_col = 3075
idx = row_col_to_idx(target_row, target_col)

code = 20151125
for _ in xrange(idx - 1):
    code *= 252533
    code %= 33554393

print 'part 1:', code
