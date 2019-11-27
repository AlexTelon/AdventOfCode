import itertools


class path(frozenset):
    """A path is represented by a frozenset.

    The distance is symmetrical.
    a -> b == b -> a

    The representation of a path between two cities a and b should
    therfore not take order into account. Hence a set.

    Frozenset is a immutable set which means it can like tuple be
    used as a key in a dictionary. (Remember dictionaries are hashmaps).
    So the hash of a frozenset depends on the data, not the order.
    """
    def __new__(cls, *cities):
        # This function allows us to initialize with the cities as a list of arguments.
        # without this: path([a, b])
        # with this:    path(a, b)
        return frozenset.__new__(cls, cities)


def parse_data():
    """Reads from input file and returns list of tuples.

    Example:
        "Faerun to Tristram = 65" -> ("Faerun", "Tristram", 65)
    """
    with open('input.txt') as f:
        data = [line.split() for line in f]

    parsed_data = []
    for origin, _, destination, _, dist in data:
        parsed_data.append((origin, destination, int(dist)))
    return parsed_data
    # return [(a, b, int(dist)) for a, _, b, _, dist in data]

def get_cities(data):
    """Gives a set of all cities mentioned in the data."""
    cities = set()
    for origin, destination, _ in data:
        cities.add(origin)
        cities.add(destination)
    return cities

def city_distances(data):
    """Creates a dictionary of where a path is the key and the value is the distance.

    Example:
        {
            path("Faerun", "Tristram"): 65,
            path("Tristram", "Tambi"): 63,
        }
    """
    result = {}
    for origin, destination, dist in data:
        result[path(origin, destination)] = dist
    return result


def get_distance(*destinations):
    total = 0
    # loop over all destinations pairwise
    for start, stop in zip(destinations, destinations[1:]):
        total += city_distances[path(start, stop)]
    return total


data = parse_data()
cities = get_cities(data)
city_distances = city_distances(data)

costs = {}
for c in itertools.permutations(cities):
    costs[c] = get_distance(*c)

print(f"nr of cities: {len(cities)}, nr of solutions {len(costs)}")
print(f"min: {min(costs.values())}")
print(f"max: {max(costs.values())}")