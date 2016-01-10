with open('input.txt', 'r') as fh:
    moves = [1 if m == '(' else -1 for m in fh.readline().strip()]

print 'part 1', sum(moves)

pos = 0
for step, move in enumerate(moves):
    if pos == -1:
        print 'part 2', step
        break
    pos += move
