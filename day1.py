import numpy as np

with open('day1.txt', 'r') as fh:
    moves = [1 if m == '(' else -1 for m in fh.readline().strip()]

print 'part 1', sum(moves)
print 'part 2', np.cumsum(moves).tolist().index(-1) + 1
