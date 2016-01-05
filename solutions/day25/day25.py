def lazy_caterer(n):
    return (n ** 2 + n + 2) / 2


def row_col_to_idx(row, col):
    row -= 1
    col -= 1
    return lazy_caterer(row + col) + col


target_row = 2981
target_col = 3075
idx = row_col_to_idx(target_row, target_col)

code = 20151125
for _ in xrange(idx - 1):
    code *= 252533
    code %= 33554393

print 'part 1:', code
