import itertools

containers = []
with open('input.txt', 'r') as fh:
    for line in fh:
        containers.append(int(line.strip()))

valid_combos = []
for n in xrange(1, len(containers) + 1):
    for combo in itertools.combinations(containers, n):
        if sum(combo) == 150:
            valid_combos.append(combo)
print 'part 1', len(valid_combos)

combo_lens = map(len, valid_combos)
min_num = min(combo_lens)
print 'part 2', len(filter(lambda x: x == min_num, combo_lens))
