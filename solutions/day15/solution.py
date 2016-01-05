import re
import itertools
import functools
from operator import mul
from collections import defaultdict


ingredient_to_props = defaultdict(dict)
props = 'capacity', 'durability', 'flavor', 'texture', 'calories'
with open('input.txt', 'r') as fh:
    for line in fh:
        regex = '(?P<ingredient>[\w]+): '
        regex += ', '.join('{prop} (?P<{prop}>[-0-9]+)'.format(prop=prop)
                           for prop in props)
        m = re.match(regex, line.strip())
        for prop in props:
            ingredient_to_props[m.group('ingredient')][prop] = int(m.group(prop))


def combo_to_prop_sum(combo, prop):
    s = sum([pct * ingredient_to_props[ingredient][prop]
             for ingredient, pct in zip(ingredient_to_props.keys(), combo)])
    return max(0, s)


def combo_to_score(combo):
    scoring_props = [p for p in props if p != 'calories']
    scores = map(functools.partial(combo_to_prop_sum, combo), scoring_props)
    return reduce(mul, scores)

combos = itertools.product(range(0, 101), repeat=len(ingredient_to_props.keys()))
valid_combos = filter(lambda c: sum(c) == 100, combos)
print 'part 1', max(map(combo_to_score, valid_combos))

cal500_combos = filter(lambda c: combo_to_prop_sum(c, 'calories') == 500, valid_combos)
print 'part 2', max(map(combo_to_score, cal500_combos))
