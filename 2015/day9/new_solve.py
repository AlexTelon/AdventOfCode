import itertools


def dist(*cities):
    """Calculates the total distance between any number of cities"""
    if len(cities) == 2:
        return city_distances[frozenset([cities[0], cities[1]])]

    # Loop over all cities pairwise and sum the pairwise distances.
    return sum(dist(a,b) for a, b, in zip(cities, cities[1:]))


with open('input.txt') as f:
    data = [line.split() for line in f]

cities = set()
# A dictionary of all given city a-b combinations and the distances between them.
city_distances = {}
for a, _, b, _, distance in data:
    cities.update({a,b})
    city_distances[frozenset([a, b])] = int(distance)

# Calculate the cost of all permutations of cities in a dictionary.
costs = { path:dist(*path) for path in itertools.permutations(cities) }

print(f"min: {min(costs.values())} max: {max(costs.values())}")