import itertools

def get_distance(*destinations):
    return sum(city_distances[frozenset([a,b])] for a, b, in zip(destinations, destinations[1:]))

# Transform data to a list of tuples. Example: ("Faerun", "Tristram", 65).
with open('input.txt') as f:
    data = [(a, b, int(dist)) for a, _, b, _, dist in [line.split() for line in f]]

# Write the data into a dictionary. Key is a set of two cities and value is the distance between the two.
city_distances = { frozenset([origin, destination]):dist for origin, destination, dist in data }

# Calculate the cost of all permutations of cities
costs = {perm:get_distance(*perm) for perm in itertools.permutations({city for a, b, _ in data for city in (a, b)})}

print(f"min: {min(costs.values())}, max: {max(costs.values())}")