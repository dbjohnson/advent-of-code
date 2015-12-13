import itertools
import numpy as np


def paper_required(dims):
    dims = map(int, dims.split('x'))
    sides = [np.prod(s) for s in itertools.combinations(dims, 2)]
    return sum([2*s for s in sides]) + min(sides)


def ribbon_required(dims):
    dims = map(int, dims.split('x'))
    maxdim = max(dims)
    area = np.prod(dims)
    dims.remove(maxdim)
    perim = sum([2 * dim for dim in dims])
    return area + perim


with open('day2.txt', 'r') as fh:
    print 'part 1', sum([paper_required(l.strip()) for l in fh])

with open('day2.txt', 'r') as fh:
    print 'part 2', sum([ribbon_required(l.strip()) for l in fh])
