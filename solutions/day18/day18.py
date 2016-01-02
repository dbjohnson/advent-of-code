class Automata(object):
    def __init__(self, row, col, state):
        self.row = row
        self.col = col
        self.init_state = state
        self.state = state
        self.neighbors = []

    def connect(self, neighbor):
        self.neighbors.append(neighbor)

    def calc_next_state(self):
        on_count = sum(1 if n.state else 0 for n in self.neighbors)
        if self.state:
            self.next_state = on_count in (2, 3)
        else:
            self.next_state = on_count == 3

    def update(self):
        self.state = self.next_state

    def reset(self):
        self.state = self.init_state

world = []
with open('input.txt', 'r') as fh:
    for i, line in enumerate(fh):
        world.append([Automata(i, j, c == '#') for j, c in enumerate(line.strip())])

for i, row in enumerate(world):
    for j, a in enumerate(row):
        for ii in xrange(max(0, i - 1), min(len(world), i + 2)):
            for jj in xrange(max(0, j - 1), min(len(row), j + 2)):
                if ii != i or jj != j:
                    a.connect(world[ii][jj])


everyone = reduce(lambda x, y: x + y, world)
for step in xrange(100):
    for a in everyone:
        a.calc_next_state()
    for a in everyone:
        a.update()
print 'part 1', sum(1 if a.state else 0 for a in everyone)


working = []
for a in everyone:
    if a.row in (0, 99) and a.col in (0, 99):
        a.state = True
    else:
        a.reset()
        working.append(a)

for step in xrange(100):
    for a in working:
        a.calc_next_state()
    for a in working:
        a.update()
print 'part 2', sum(1 if a.state else 0 for a in everyone)
