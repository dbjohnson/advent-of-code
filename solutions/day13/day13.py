import re
from Queue import PriorityQueue
from collections import defaultdict

seating_costs = defaultdict(lambda: defaultdict(int))
with open('input.txt', 'r') as fh:
    for line in fh:
        m = re.match('(?P<p1>\w+) would (?P<sign>gain|lose) (?P<points>[0-9]+) happiness units by sitting next to (?P<p2>\w+).', line.rstrip())
        seating_costs[m.group('p1')][m.group('p2')] = int(m.group('points')) * (1 if m.group('sign') == 'gain' else -1)

mindist = min([min(dists.values()) for c, dists in seating_costs.items()])
floored_costs = defaultdict(lambda: defaultdict(int))
for p1, p2s in seating_costs.items():
    for p2, c in p2s.items():
        floored_costs[p1][p2] = c - mindist + 1


def path_cost(path, cost_matrix):
    if len(path) < 2:
        return 0
    p = path[:] + [path[0]]  # complete circle
    return sum([cost_matrix[p[i]][p[i + 1]] + cost_matrix[p[i + 1]][p[i]]
                for i in xrange(len(p) - 1)])


def Astar(start, goal, cost_matrix, strategy='minimize'):
    mindist = min([min(dists.values()) for c, dists in cost_matrix.items()])
    maxdist = max([max(dists.values()) for c, dists in cost_matrix.items()])
    def cost_fn(path):
        if strategy == 'minimize':
            return path_cost(path, cost_matrix) + (len(cost_matrix.keys()) - len(path)) * 2 * mindist
        else:
            return -(path_cost(path, cost_matrix) + (len(cost_matrix.keys()) - len(path)) * 2 * maxdist)
    abort_cost = 1 << 32
    q = PriorityQueue()
    q.put((cost_fn([start]), [start]))
    best_path = []
    while not q.empty():
        total_cost, partial_path = q.get()
        if total_cost > abort_cost:
            break
        if partial_path[-1] == goal and len(partial_path) == len(cost_matrix.keys()):
            if total_cost < abort_cost:
                abort_cost = total_cost
                best_path = partial_path
        else:
            for c in cost_matrix[partial_path[-1]]:
                if c not in partial_path:
                    new_path = partial_path + [c]
                    total_cost = cost_fn(new_path)
                    if total_cost < abort_cost:
                        q.put((total_cost, new_path))
    return best_path

best_path = []
start = seating_costs.keys()[0]
for end in seating_costs.keys():
    if start != end:
        path = Astar(start, end, floored_costs, 'maximize')
        if not best_path or path_cost(path, seating_costs) > path_cost(best_path, seating_costs):
            best_path = path
print 'part 1', best_path, path_cost(best_path, seating_costs)


## part 2
for guest in seating_costs.keys():
    seating_costs['me'][guest] = seating_costs[guest]['me'] = 0

mindist = min([min(dists.values()) for c, dists in seating_costs.items()])
floored_costs = defaultdict(lambda: defaultdict(int))
for p1, p2s in seating_costs.items():
    for p2, c in p2s.items():
        floored_costs[p1][p2] = c - mindist + 1

best_path = []
start = 'me'
for end in seating_costs.keys():
    if start != end:
        path = Astar(start, end, floored_costs, 'maximize')
        if not best_path or path_cost(path, seating_costs) > path_cost(best_path, seating_costs):
            best_path = path
print 'part 2', best_path, path_cost(best_path, seating_costs)
