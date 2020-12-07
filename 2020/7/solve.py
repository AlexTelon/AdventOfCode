import networkx as nx

all_bags = {}

def parse_bags(line):
    bags = []

    line = line.replace(",", "").replace(".", "")
    terms = line.split("contain")
    for term in terms:
        term = term.replace("bags", "bag")
        for bag in term.split("bag"):
        # for bag in re.split('bag |bags', bag):
            num = 1
            if any(c.isdigit() for c in bag):
                num = int("".join(c for c in bag if c.isdigit()))
            for c in "0123456789":
                bag = bag.replace(c, "")
            bag = bag.strip()
            if bag == "":
                continue
            bags.append((bag, num))
    return bags


all_stuff = []
lines = open('input.txt').read().splitlines()
for line in lines:
    bags = parse_bags(line)
    assert bags[0] not in all_bags
    all_bags[bags[0]] = bags[1:]
    all_stuff.append(bags)

g = nx.DiGraph()
for bags in all_stuff:
    edges = []
    a = bags[0][0]
    for name, cost in bags[1:]:
        edges.append((a, name, cost))
    g.add_weighted_edges_from(edges)


tot = 0
for outer, num in all_bags.keys():
    if outer == "shiny gold":
        continue
    if nx.has_path(g, source=outer, target='shiny gold'):
        tot += 1
print("part1:", tot)


def get_total_nr_of_bags(name, total=0):
    if name == "no other":
        return 0
    bags = all_bags[(name, 1)]
    for child_name, count in bags:
        # print(child_name, count)
        child_bag_count = get_total_nr_of_bags(child_name)
        total += count * child_bag_count
        # print(f"{child_name}: {count} * {child_name}({child_bag_count})")
    return total + 1

# remove -1 because we ask how many should the shiny gold one contain
print("part2", get_total_nr_of_bags('shiny gold') - 1)