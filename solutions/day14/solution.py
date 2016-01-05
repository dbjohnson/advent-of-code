import re
from collections import defaultdict


def make_t_to_dist_fn(speed, t_fly, t_rest):
    def foo(t):
        if t <= t_fly + t_rest:
            return speed * max(0, min(t, t_fly))
        else:
            return speed * t_fly + foo(t - (t_fly + t_rest))
    return foo

reindeer_to_dist_fn = {}
with open('input.txt', 'r') as fh:
    for line in fh:
        m = re.match(r'(?P<name>[\w]+) can fly (?P<speed>[0-9]+) km/s for (?P<t_fly>[0-9]+) seconds, but then must rest for (?P<t_rest>[0-9]+) seconds.', line.strip())
        reindeer_to_dist_fn[m.group('name')] = make_t_to_dist_fn(int(m.group('speed')),
                                                                 int(m.group('t_fly')),
                                                                 int(m.group('t_rest')))

winner = max(reindeer_to_dist_fn, key=lambda r: reindeer_to_dist_fn[r](2503))
print 'part 1', winner, reindeer_to_dist_fn[winner](2503)


reindeer_to_score = defaultdict(int)
for t in xrange(2503):
    dist_to_reindeer = defaultdict(list)
    for r, df in reindeer_to_dist_fn.items():
        dist_to_reindeer[df(t + 1)].append(r)
    for leader in dist_to_reindeer[max(dist_to_reindeer.keys())]:
        reindeer_to_score[leader] += 1

r = max(reindeer_to_score, key=lambda r: reindeer_to_score[r])
print 'part 2', r, reindeer_to_score[r]
