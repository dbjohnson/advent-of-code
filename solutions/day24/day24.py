import operator
import itertools
from collections import defaultdict
from Queue import Queue


with open('input.txt', 'r') as fh:
    package_weights = map(int, fh.read().split())


class Group(object):
    def __init__(self, packages):
        self.packages = packages
        self.weight = sum([package_weights[p] for p in self.packages])

    def expand(self):
        return [Group(self.packages + [i])
                for i in xrange(self.packages[-1] + 1, len(package_weights))]

    def disjoint(self, other):
        return len(set(self.packages).difference(set(self.packages))) == 0

    def quantum_entanglement(self):
        return reduce(operator.mul, [package_weights[p] for p in self.packages])

    def size(self):
        return len(self.packages)


def find_valid_groups(group_weight):
    q = Queue()
    for i in xrange(len(package_weights)):
        q.put(Group([i]))

    valid_groups = []
    while not q.empty():
        g = q.get()
        if g.weight == group_weight:
            valid_groups.append(g)
        else:
            for child in g.expand():
                if child.weight <= group_weight:
                    q.put(child)

    return valid_groups


def find_ideal_config(num_groups):
    group_weight = sum(package_weights) / num_groups
    valid_groups = find_valid_groups(group_weight)

    size_to_groups = defaultdict(list)
    for g in valid_groups:
        size_to_groups[g.size()].append(g)

    for size in sorted(size_to_groups):
        for g1 in sorted(size_to_groups[size], key=lambda g: g.quantum_entanglement()):
            groups = [g1]
            for n in xrange(num_groups - 1):
                for gn in valid_groups:
                    if all(ga.disjoint(gb) for ga, gb in itertools.combinations(groups, 2)):
                        groups.append(gn)
                        if len(groups) == num_groups:
                            return g1.quantum_entanglement()


print 'Warning - this takes a few minutes'
print 'part 1:', find_ideal_config(3)
print 'part 2:', find_ideal_config(4)
