from collections import defaultdict
from Queue import PriorityQueue

city_to_city_dist = defaultdict(lambda: defaultdict(int))
dists = set()
with open('day9.txt', 'r') as fh:
    for line in fh:
        cities, dist = line.strip().split(' = ')
        c1, c2 = cities.split(' to ')
        city_to_city_dist[c1][c2] = city_to_city_dist[c2][c1] = int(dist)
        dists.add(int(dist))


def path_cost(path, cost_matrix):
    return sum([cost_matrix[path[i]][path[i + 1]]
                for i in xrange(len(path) - 1)])


def Astar(start, goal, cost_matrix, strategy='minimize'):
    mindist = min([min(dists.values()) for c, dists in cost_matrix.items()])
    maxdist = max([max(dists.values()) for c, dists in cost_matrix.items()])

    def cost_fn(path):
        if strategy == 'minimize':
            return path_cost(path, cost_matrix) + (len(cost_matrix.keys()) - len(path) - 1) * mindist
        else:
            return -(path_cost(path, cost_matrix) + (len(cost_matrix.keys()) - len(path) - 1) * maxdist)

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

shortest_path = None
for c1 in city_to_city_dist.keys():
    for c2 in city_to_city_dist[c1]:
        path = Astar(c1, c2, city_to_city_dist, 'minimize')
        if path and (not shortest_path or path_cost(path, city_to_city_dist) < path_cost(shortest_path, city_to_city_dist)):
            shortest_path = path
print 'part 1', path_cost(shortest_path, city_to_city_dist), shortest_path


longest_path = None
for c1 in city_to_city_dist.keys():
    for c2 in city_to_city_dist[c1]:
        path = Astar(c1, c2, city_to_city_dist, 'maximize')
        if path and (not longest_path or path_cost(path, city_to_city_dist) > path_cost(longest_path, city_to_city_dist)):
            longest_path = path
print 'part 2', path_cost(longest_path, city_to_city_dist), longest_path
