import itertools
import operator


def dims_to_sides(dims):
    return itertools.combinations(dims, 2)


def paper_required(dims):
    side_dims = dims_to_sides(dims)
    side_areas = map(lambda s: reduce(operator.mul, s), side_dims)
    return sum(side_areas) * 2 + min(side_areas)


def ribbon_required(dims):
    side_dims = dims_to_sides(dims)
    perimeters = map(lambda s: reduce(operator.add, s), side_dims)
    volume = reduce(operator.mul, dims)
    return volume + min(perimeters) * 2


with open('input.txt', 'r') as fh:
    input = map(lambda line: map(int, line.split("x")), fh.read().split())

print('part 1: {}'.format(sum(map(paper_required, input))))
print('part 1: {}'.format(sum(map(ribbon_required, input))))
