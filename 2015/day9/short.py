import itertools

def get_distance(*destinations):
    return sum(city_distances[frozenset([a,b])] for a, b, in zip(destinations, destinations[1:]))

with open('input.txt') as f:
    data = [line.split() for line in f]
data = [(a, b, int(dist)) for a, _, b, _, dist in data]

cities = {x for a, b, _ in data for x in (a, b)}

city_distances = { frozenset([origin, destination]):dist for origin, destination, dist in data }

costs = {perm:get_distance(*perm) for perm in itertools.permutations(cities)}

print(f"nr of cities: {len(cities)}, nr of solutions {len(costs)}")
print(f"min: {min(costs.values())}")
print(f"max: {max(costs.values())}")