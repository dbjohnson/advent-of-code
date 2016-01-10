with open('input.txt', 'r') as fh:
    moves = [1 if m == '(' else -1 for m in fh.readline().strip()]

print 'part 1', sum(moves)

pos = 0
for i, move in enumerate(moves):
    pos += move
    if pos == -1:
        print 'part 2', i + 1
        break
