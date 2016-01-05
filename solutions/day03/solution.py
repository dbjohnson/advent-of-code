with open('input.txt', 'r') as fh:
    route = fh.readline()

m_to_idx = {'^': 0,
            'v': 0,
            '>': 1,
            '<': 1}
m_to_sign = {'^': 1,
             'v': -1,
             '>': 1,
             '<': -1}

pos = [0, 0]
visited = set()
visited.add(str(pos))
for m in route:
    pos[m_to_idx[m]] += m_to_sign[m]
    visited.add(str(pos))

print 'part 1', len(visited)

## part 2

pos1 = [0, 0]
pos2 = [0, 0]
visited = set()
visited.add(str(pos1))

for i, m in enumerate(route):
    if i % 2:
        pos = pos1
    else:
        pos = pos2

    pos[m_to_idx[m]] += m_to_sign[m]
    visited.add(str(pos))

print 'part 2', len(visited)
