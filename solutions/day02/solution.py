import itertools
import numpy as np


def paper_required(dims):
    dims = map(int, dims.split('x'))
    sides = [np.prod(s) for s in itertools.combinations(dims, 2)]
    return sum([2 * s for s in sides]) + min(sides)


def ribbon_required(dims):
    dims = map(int, dims.split('x'))
    maxdim = max(dims)
    area = np.prod(dims)
    dims.remove(maxdim)
    perim = sum([2 * dim for dim in dims])
    return area + perim


with open('input.txt', 'r') as fh:
    input = fh.read().split()


print('part 1: {}'.format(sum(map(paper_required, input))))
print('part 1: {}'.format(sum(map(ribbon_required, input))))
