import itertools


class solve():

    def __init__(self):
        with open('input.txt') as f:
            data = [line.split() for line in f]

        cities = set()
        # A dictionary of all given city a-b combinations and the distances between them.
        self.city_distances = {}
        for a, _, b, _, dist in data:
            cities.update({a,b})
            self.city_distances[frozenset([a, b])] = int(dist)

        # Calculate the cost of all permutations of cities in a dictionary.
        self.costs = { path:self.dist(*path) for path in itertools.permutations(cities) }

    def dist(self, *destinations):
        """Calculates the total distance between any number of cities"""
        if len(destinations) == 2:
            return self.city_distances[frozenset([destinations[0], destinations[1]])]

        # Loop over all destinations pairwise and sum the pairwise distances.
        return sum(self.dist(a,b) for a, b, in zip(destinations, destinations[1:]))


if __name__ == "__main__":
    solution = solve()
    print(f"min: {min(solution.costs.values())} max: {max(solution.costs.values())}")