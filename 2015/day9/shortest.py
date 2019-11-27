import itertools
# Transform data to a list of tuples. Example: ("Faerun", "Tristram", 65).
data = [(a, b, int(dist)) for a, _, b, _, dist in [line.split() for line in open('input.txt')]]
# Write the data into a dictionary. Key is a set of two cities and value is the distance between the two.
city_distances = { frozenset([origin, destination]):dist for origin, destination, dist in data }
# Calculate the cost of all permutations of cities
costs = {perm:sum(city_distances[frozenset([a,b])] for a, b, in zip(perm, perm[1:])) for perm in itertools.permutations({city for a, b, _ in data for city in (a, b)})}
print(f"min: {min(costs.values())}, max: {max(costs.values())}")