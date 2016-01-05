total = 0
real = 0
with open('input.txt', 'r') as fh:
    for line in fh:
        total += len(line.strip())
        real += len(eval(line.strip()))
print 'part 1: {}'.format(total - real)

total = 0
encoded = 0
with open('input.txt', 'r') as fh:
    for line in fh:
        l = len(line.strip())
        total += l
        encoded += l + line.count('"') + line.count('\\') + 2
print 'part 2: {}'.format(encoded - total)
