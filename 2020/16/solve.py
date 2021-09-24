from collections import defaultdict
# part 2, part1 is found in git history (previous commit)

# lines = open('input.txt').read().splitlines()
lines = open(0).read().splitlines()
lines = [[int(x) for x in line.split(',')] for line in lines]

rules_dict = {
    'departure_location': [(32,209), (234,963)],
    'departure_station': [(47,64), (83,967)],
    'departure_platform': [(37,609), (628,970)],
    'departure_track': [(29,546), (567,971)],
    'departure_date': [(50,795), (816,960)],
    'departure_time': [(49,736), (750,962)],
    'arrival_location': [(48,399), (420,967)],
    'arrival_station': [(49,353), (360,967)],
    'arrival_platform': [(37,275), (298,969)],
    'arrival_track': [(40,119), (127,954)],
    'class_': [(35,750), (760,968)],
    'duration': [(43,162), (186,963)],
    'price': [(30,889), (914,949)],
    'route': [(39,266), (274,950)],
    'row': [(45,366), (389,954)],
    'seat': [(42,765), (772,955)],
    'train': [(30,494), (518,957)],
    'type_': [(48,822), (835,973)],
    'wagon': [(32,330), (342,951)],
    'zone': [(36,455), (462,973)],
}

my_ticket = [109,137,131,157,191,103,127,53,107,151,61,59,139,83,101,149,89,193,113,97]

def check_num_against_rules(x):
    for ranges in rules_dict.values():
        if any(lo <= x <= hi for lo, hi in ranges):
            return True
    return False


passing = [line for line in lines if all(check_num_against_rules(x) for x in line)]

def check_ranges(x, ranges):
    return any(lo <= x <= hi for lo, hi in ranges)

solutions = defaultdict(list)
for i in range(len(passing[0])):
    values = [p[i] for p in passing]

    # First find all rules which this set of values are valid against.
    for name, ranges in rules_dict.items():
        if all(check_ranges(v, ranges) for v in values):
            solutions[name].append(i)

# Now figure a way such that all rules have 1 index.
# Idea is to remove from all others when a rule only passes for 1 index.
solution = {}
while not all(len(v) == 1 for k,v in solutions.items()):
    for k, indexes in solutions.items():

        if len(indexes) == 1 and k not in solution:
            index = indexes[0]
            solution[k] = index

            # Remove this from others.
            for inner_k, indexes in solutions.items():
                if inner_k == k:
                    continue
                if index in solutions[inner_k]:
                    solutions[inner_k].remove(index)

ans2 = 1
for k,v in solution.items():
    if k.startswith('departure'):
        print(k, v)
        ans2 *= my_ticket[v]
print(ans2)