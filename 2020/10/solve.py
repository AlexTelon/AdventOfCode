from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat
from os import remove
import queue
from threading import Thread
from collections import deque
from decimal import Decimal
from fractions import Fraction
import fractions
import string
import operator


import math

adapters = open('input.txt').read().splitlines()
adapters = sorted([int(adapter) for adapter in adapters])
# for adapter in sorted(adapters):
#     print(adapter)

# 1 2 3 lower ans still produce its output. 0 should be fine too then.

# built in +3 higher than max


prev = 0
# for a,b in zip(adapters, adapters[1:]):
diffs = defaultdict(int)

for current in adapters:
    diff = current - prev
    diffs[diff] += 1
    # print(current, " diff ", diff)
    prev = current

# buitl int
diffs[3] += 1

# print(adapters)

# print()
# for k,v in diffs.items():
#     print(k, v)
print("part1", diffs[1] * diffs[3])


# part 2

# What is the total number of distinct ways you can arrange the adapters to connect the charging outlet to your device?

# count = Counter(adapters)
# for k,v in count.items():
#     print(k,v)

# we always start at 0
adapters.append(max(adapters) + 3)
# print("len", len(adapters))
# adapters = deque(adapters)


# prev = 0
# arr = 1
# while len(adapters) > 0:
#     upcomming = [x for x in adapters if x - prev <= 3]
#     n = len(upcomming)
#     combs = list(combinations(upcomming, r=n-1))
#     prev = max(upcomming)
#     for x in upcomming:
#         adapters.remove(x)
#     # print("combs", list(combinations(upcomming, r=n)))
#     mult = max(1,len(combs))
#     print("upcomming: ", upcomming, "comb:", combs, "mult:", mult)
#     arr *= mult

def is_valid(adapters):
    diffs = defaultdict(int)
    prev = 0
    for current in adapters:
        diff = current - prev
        diffs[diff] += 1
        if diff > 3:
            return False
        # print(current, " diff ", diff)
        prev = current
    return True

def is_valid2(adapters, removed):
    prev = 0
    for current in adapters:
        if current in removed:
            continue
        diff = current - prev
        # diffs[diff] += 1
        if diff > 3:
            return False
        # print(current, " diff ", diff)
        prev = current
    return True

upcomming_all = defaultdict(list)
for i, current in enumerate(adapters[:-1]):
    upcomming = [x for x in adapters[i+1:] if x - current <= 3]
    upcomming_all[current] = upcomming
# special for first iteration
upcomming = [x for x in adapters if x <= 3]
upcomming_all[0] = upcomming

print(upcomming_all)



removed_all = []
for adapter in reversed(adapters[:-1]):
    tmp = adapters.copy()
    tmp.remove(adapter)
    if is_valid(tmp):
        removed_all.append(adapter)
        # print(f'can remove {adapter} {tmp}')

print()
print('remove', removed_all)
# prune upcomming all a bit
upcomming_all_pruned = defaultdict(list)
for key, values in upcomming_all.items():
    if not any(x in removed_all for x in values):
        continue
    upcomming_all_pruned[key] = values

# print('pruned upcomming all', upcomming_all_pruned, "len", len(upcomming_all_pruned))
# print('upcomming all', upcomming_all, "len", len(upcomming_all))

def is_valid3(adapters, removed):
    for key, upcomming, in upcomming_all_pruned.items():
        if all(x in removed for x in upcomming):
            # print(f'all for {key} [{upcomming}] removed by {removed}')
            return False
    return True

diff_to_next = defaultdict(int)
# for a,b in zip(adapters, adapters[1:]):
#     diff = b-a
#     diff_to_next[a] = diff
removed_all.append(math.inf)
groups = []
prev = removed_all[0]
this_group = []
for current in sorted(removed_all):
    diff = current - prev
    # diffs[diff] += 1
    if diff > 3:
        
        ways_to_remove = 0
        for r in range(1, len(this_group)+1):
            for removed in combinations(this_group, r=r):
                if is_valid2(adapters, removed):
                    ways_to_remove += 1
        
        groups.append((this_group, ways_to_remove))

        this_group = []
    # print(current, " diff ", diff)
    this_group.append(current)
    prev = current

print("groups", groups)
# count the ways in which to indepentently remove in smaller groups
ans = 1
for group, combs in groups:
    print(group, "multi is the factor that tells how many ways items from this group can be removed validly:", combs)
    ans *= combs

print("^^^^^^^^^^^^^")
n = len(groups)
print("len of groups", n)

# if False:
ways_to_remove = 0
for r in range(len(groups)+1):
    for removed in combinations(groups, r=r):
        multi = 1
        for group, combs in removed:
            multi *= combs
        #     # if isinstance(group, list):
            #     flat_removed.extend(group)
            # else:
            #     flat_removed.append(group)
        # print(flat_removed)
        # if is_valid2(adapters, flat_removed):
        #     print("flat_removed that worked", flat_removed)
            # ways_to_remove *= ways
        ways = multi
        # print(removed, multi, ways, len(removed))
        ways_to_remove += ways
print('alex new solution', ways_to_remove)
exit()
print()
print(ans * math.factorial(len(groups)))
print("fac of group size", math.factorial(len(groups)))
print(ans)
print()


ans = 0
for r in range(len(removed_all)+1):
    # need to reduce number of combinations!!!
    for removed in combinations(removed_all, r=r):
        if is_valid2(adapters, removed):
            # print("can remove ", removed)
            ans += 1
    
print('remove len', len(removed_all), "possibilities max", 2**len(removed_all))
print("part2", 2**len(removed_all))
print("part2", ans)
exit()

# print(arr)
prev = 0
arr = 1
# exit()
upcomming_all = defaultdict(list)
for i, current in enumerate(adapters):
    upcomming = [x for x in adapters[i+1:] if x - current <= 3]
    upcomming_all[current] = upcomming

# for k,v in upcomming_all.items():
#     print(k,v)
# print(upcomming_all)
# exit()


adapters = deque(adapters)
while len(adapters) > 0:
    upcomming = [x for x in adapters if x - prev <= 3]
    n = len(upcomming)
    print(f"upcomming: {upcomming}, {n}")
    # combs = list(combinations(upcomming, r=n-1))
    prev = min(upcomming)
    adapters.remove(prev)
    # print("combs", list(combinations(upcomming, r=n)))
    # mult = max(1,len(combs))

    arr *= n

print(arr)

# not 999502313552216064
# not 17592186044416