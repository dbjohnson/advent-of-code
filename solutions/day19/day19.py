import re
from Queue import PriorityQueue


class Molecule(object):
    def __init__(self, molecule, edits=0):
        self.molecule = molecule
        self.edits = edits
        self.atoms = re.findall('[A-Z][a-z]*|e', self.molecule)

    def derivatives(self, substitutions):
        children = set()
        for s1, s2 in substitutions:
            for m in re.finditer(s1, self.molecule):
                molecule = self.molecule[:m.start()] + s2 + self.molecule[m.end():]
                children.add(Molecule(molecule, self.edits + 1))
        return children

    def __hash__(self):
        return hash(self.molecule)

    def __eq__(self, other):
        return hash(self) == hash(other)

    def __len__(self):
        return len(self.atoms)

    def __cmp__(self, other):
        return len(self) - len(other)


substitutions = []
with open('input.txt', 'r') as fh:
    for line in fh:
        if ' => ' in line:
            atom, sub = line.strip().split(' => ')
            substitutions.append((atom, sub))
        elif line:
            medicine = Molecule(line.strip())

print 'part 1:', len(medicine.derivatives(substitutions))


# For part 2, use greedy search to shrink the molecule as quickly as possible
# until we get to the seed molecule.  To be fair, this doesn't strictly guarantee
# the shortest possible solution.
reverse_substitutions = [(s2, s1) for s1, s2 in substitutions]
seed = Molecule('e')
q = PriorityQueue()
q.put(medicine)
while not q.empty():
    m = q.get()
    if m == seed:
        print 'part 2:', m.edits
        break
    for c in m.derivatives(reverse_substitutions):
        q.put(c)
