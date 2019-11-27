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
    return [(a, b, int(dist)) for a, _, b, _, dist in data]


def get_cities(data):
    """Gives a set of all cities mentioned in the data."""
    return {x for a, b, _ in data for x in (a, b)}


def city_distances(data):
    """Creates a dictionary of where a path is the key and the value is the distance.

    Example:
        {
            path("Faerun", "Tristram"): 65,
            path("Tristram", "Tambi"): 63,
        }
    """
    return { path(origin, destination):dist for origin, destination, dist in data }


def dist(a, b):
    """Calculates the distance between two cities"""
    return city_distances[path(a, b)]


def get_distance(*destinations):
    """Calculates the distance when traversing all destinations"""
    # [a,b,c, ...] -> sum([dist(a,b), dist(b,c), ...])
    return sum(dist(a,b) for a, b, in zip(destinations, destinations[1:]))


data = parse_data()
cities = get_cities(data)
city_distances = city_distances(data)

costs = {perm:get_distance(*perm) for perm in itertools.permutations(cities)}

print(f"nr of cities: {len(cities)}, nr of solutions {len(costs)}")
print(f"min: {min(costs.values())}")
print(f"max: {max(costs.values())}")