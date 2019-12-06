from collections import defaultdict


data = [line.strip().split(')') for line in open('input.txt')]

parents = defaultdict(set)

names = set()
for a, b in data:
    parents[b].add(a)

    names.add(a)
    names.add(b)

def count_parents(name):
    if name == 'COM':
        return 0

    total = 1
    for parent in parents[name]:
        total += count_parents(parent)
    return total

    # return 1 + sum(count_parents(p) for p in parents[name])

def get_all_parents(name):
    if name == 'COM':
        return []
    
    result = set()

    for parent in parents[name]:
        result.add(parent)
        result.update(get_all_parents(parent))
    return result



# Distances to COM.
distances = defaultdict(int)
# Paths to COM.
pahts = defaultdict(set)

# Part 1: the total number of direct and indirect orbits
total = 0

for name in names:
    if name == 'COM':
        continue

    dist = count_parents(name)
    pahts[name] = get_all_parents(name)
    total += dist

    distances[name] = dist

me = pahts['YOU']
santa = pahts['SAN']

same_path = me.intersection(santa)

common_cost = len(same_path)

print('part2: ', distances['YOU'] + distances['SAN'] - 2 * common_cost) 

print('part1: ', total)