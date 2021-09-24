from collections import defaultdict
from itertools import combinations
import math

adapters = open('input.txt').read().splitlines()
adapters = sorted([int(adapter) for adapter in adapters])

prev = 0
diffs = defaultdict(int)
for current in adapters:
    diff = current - prev
    diffs[diff] += 1
    prev = current

# Add the built in one
diffs[3] += 1

print("part1", diffs[1] * diffs[3])


# part 2

# What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?

# Add the extra adapter that is built-in to the machine.
adapters.append(max(adapters) + 3)

def is_valid(adapters, removed=None):
    if removed is None:
        removed = []
    prev = 0
    for current in adapters:
        if current in removed:
            continue
        diff = current - prev
        if diff > 3:
            return False

        prev = current
    return True

def combinations_all_r(things):
    for r in range(1, len(things)+1):
        for comb in combinations(things, r=r):
            yield comb

removed_all = [removed for removed in reversed(adapters[:-1]) if is_valid(adapters, [removed])]

groups = []
removed_all = sorted(removed_all)
prev = removed_all[0]
this_group = [prev]
for prev, current in zip(removed_all, removed_all[1:] + [math.inf]):
    diff = current - prev
    if diff > 3:
        # Number of valid removal combinations done within the group that dont break the validity of the whole.
        valid_removes = sum(is_valid(adapters, removed) for removed in combinations_all_r(this_group))
        groups.append((this_group, valid_removes))

        this_group = []

    this_group.append(current)

# info/debug
print()
print(f"{'independent groups':<20}valid_combinations")
for group, valid_combinations in groups:
    print(f"{str(group):<20}{str(valid_combinations)}")
print()

# combinations_all_r gives all combinations for all lengths r for r in 1..n
# combinations_all_r([1, 2, 3]) - > [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)]
# What we have is not 1, 2 etc, but groups of numbers that we have previously decided are independent.
# Meaning removing one from one group does not affect the validity of other group choices
# Futhermore for each independent group we have stored the number of valid combinations it has.
# For example ([1, 2, 3], 6) means that the 6 out of the 7 combinations in [(1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3)] are valid.
# which ones are valid does not matter. (but probably its (1,2,3) as removing all is too much and would result in an invalid total combination.

# Below we now do a meta-level combination of these independent combinations and we just count up how many true combinations could be made with these groups.

ways_to_remove = 0
for groups in combinations_all_r(groups):
    ways = math.prod(valid_combinations for _, valid_combinations in groups)
    ways_to_remove += ways

print('part2', ways_to_remove)