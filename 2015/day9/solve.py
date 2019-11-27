import itertools

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
for origin, destination, dist in data:
    city_distances[frozenset([origin, destination])] = dist

def get_distance(*destinations):
    total = 0
    # loop over all destinations pairwise
    for start, stop in zip(destinations, destinations[1:]):
        total += city_distances[frozenset([start, stop])]

    return total

costs = {}
for c in itertools.permutations(cities):
    costs[c] = get_distance(*c)

print(f"nr of cities: {len(cities)}, nr of solutions {len(costs)}")

print(f"min: {min(costs.values())}")
print(f"max: {max(costs.values())}")