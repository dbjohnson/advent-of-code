import re
from collections import defaultdict


clues = {'children': 3,
         'cats': 7,
         'samoyeds': 2,
         'pomeranians': 3,
         'akitas': 0,
         'vizslas': 0,
         'goldfish': 5,
         'trees': 3,
         'cars': 2,
         'perfumes': 1}

aunt_to_props = defaultdict(dict)
with open('input.txt', 'r') as fh:
    for line in fh:
        aunt = line.split(':')[0]
        for prop in re.findall('\w+: [0-9]+', line):
            prop, val = prop.split(': ')
            aunt_to_props[aunt][prop] = int(val)

for aunt, props in aunt_to_props.items():
    if all([clues[p] == v for p, v in props.items()]):
        print 'part 1', aunt

def clue_match(prop, val):
    if prop in ('cats', 'trees'):
        return val > clues[prop]
    elif prop in ('pomeranians', 'goldfish'):
        return val < clues[prop]
    else:
        return val == clues[prop]

for aunt, props in aunt_to_props.items():
    if all([clue_match(p, v) for p, v in props.items()]):
        print 'part 2', aunt
