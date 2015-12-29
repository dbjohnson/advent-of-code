import re
from collections import defaultdict
import numpy as np

with open('input.txt', 'r') as fh:
    instructions = fh.readlines()


def solve(action_to_fn):
    on = defaultdict(int)
    for instruction in instructions:
        m = re.match(r'(?P<action>toggle|turn off|turn on) (?P<xfrom>[0-9]+),(?P<yfrom>[0-9]+) through (?P<xto>[0-9]+),(?P<yto>[0-9]+)', instruction)
        action = m.group('action')
        x_from = int(m.group('xfrom'))
        y_from = int(m.group('yfrom'))
        x_to = int(m.group('xto'))
        y_to = int(m.group('yto'))
        if x_to < x_from:
            x_from, x_to = x_to, x_from

        if y_to < y_from:
            y_from, y_to = y_to, y_from

        for x in xrange(x_from, x_to + 1):
            for y in xrange(y_from, y_to + 1):
                on[(x, y)] = action_to_fn[action](on[(x, y)])

    return np.sum(on.values())


print 'part 1', solve({'toggle': lambda x: 0 if x else 1,
                       'turn on': lambda x: 1,
                       'turn off': lambda x: 0})

print 'part 2', solve({'toggle': lambda x: x + 2,
                       'turn on': lambda x: x + 1,
                       'turn off': lambda x: max(0, x - 1)})
