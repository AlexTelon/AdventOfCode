from collections import defaultdict
from pprint import pprint
import itertools

# Read data
with open('input.txt') as f:
    data = f.read().splitlines()

# remove fluff in input
data = [x.split() for x in data]
# from, to, distance
data = [(x[0], x[2], int(x[4])) for x in data]

# make sure to find all city names
cities = set((x[0] for x in data))
cities = cities.union(set((x[1] for x in data)))

city_distances = {}
for x in data:
    origin = x[0]
    destination = x[1]
    dist = x[2]

    # Save as hash instead that is order independent.
    # That way a future solution might be nicer too since it can simply find answers by looking at if the answer for a hash already exists.
    city_distances[(origin, destination)] = dist

n = len(cities)
permutations = itertools.permutations(cities, n)

def get_distance(*destinations):
    total = 0
    # loop over all destinations pairwise
    for start, stop in zip(destinations, destinations[1:]):
        key = (start, stop)
        try:
            total += city_distances[key]
        except KeyError:
            key = (stop, start)
            total += city_distances[key]

    return total


costs = {}
for c in permutations:
    costs[c] = get_distance(*c)

print(f"nr of cities: {n}")
print(f"nr of solutions: {len(costs)}")

print(f"min: {min(costs.values())}")
print(f"max: {max(costs.values())}")