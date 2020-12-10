from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat
import queue
from threading import Thread
from collections import deque
from decimal import Decimal
from fractions import Fraction
import fractions
import networkx
import string
import operator

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
    
    # print(adapters, 'max diff', max(diffs.values()))
    # return max(diffs.values()) <= 3
    return True

ans = 1
removed_all = []
for adapter in reversed(adapters[:-1]):
    tmp = adapters.copy()
    tmp.remove(adapter)
    if is_valid(tmp):
        removed_all.append(adapter)
        print(f'can remove {adapter} {tmp}')
        ans *= 2

print()
print('remove', removed_all)
# for removed in removed_all:
print('remove len', len(removed_all), "possibilities max", 2**len(removed_all))
print("part2", ans)
exit()

# print(arr)
prev = 0
arr = 1
diff_to_next = defaultdict(int)
for a,b in zip(adapters, adapters[1:]):
    diff = b-a
    diff_to_next[a] = diff
# print("next",diff_to_next)
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