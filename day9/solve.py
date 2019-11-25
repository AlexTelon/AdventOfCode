

with open('input.txt') as f:
    data = f.read().splitlines()

data = [x.split() for x in data]
data = [(x[0], x[2], int(x[4])) for x in data]

cities = set((x[0] for x in data))
cities = cities.union(set((x[1] for x in data)))

from collections import defaultdict

city_distances = defaultdict(dict)
for x in data:
    origin = x[0]
    destination = x[1]
    dist = x[2]

    # Save as hash instead that is order independent.
    # That way a future solution might be nicer too since it can simply find answers by looking at if the answer for a hash already exists.
    city_distances[(origin, destination)] = dist
    city_distances[(destination, origin)] = dist


from pprint import pprint
# pprint(city_distances)

# We need to travel to each city. Minimize the total cost

import itertools
n = len(cities)
print(f"nr of cities: {n}")
permutations = itertools.permutations(cities, n)
print(f"nr of permutations: {permutations}")

def get_distance(*destinations):
    total = 0
    # loop over all destinations pairwise
    for start, stop in zip(destinations, destinations[1:]):
        total += city_distances[(start, stop)]
    return total



costs = {}
for c in permutations:
    costs[c] = get_distance(*c)

pprint(costs)
print(f"nr of solutions: {len(costs)}")

print(min(costs.values()))



# breath first brute force
# for city in city_distances:
