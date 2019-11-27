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
    city_distances[(origin, destination)] = dist

permutations = itertools.permutations(cities, len(cities))

def get_distance(*destinations):
    total = 0
    # loop over all destinations pairwise
    for start, stop in zip(destinations, destinations[1:]):
        try:
            total += city_distances[(start, stop)]
        except KeyError:
            total += city_distances[(stop, start)]

    return total

costs = {}
for c in permutations:
    costs[c] = get_distance(*c)

print(f"nr of cities: {len(cities)}, nr of solutions {len(costs)}")

print(f"min: {min(costs.values())}")
print(f"max: {max(costs.values())}")