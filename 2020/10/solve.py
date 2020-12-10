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
    if diff > 3:
        continue
    print(current, " diff ", diff)
    prev = current

# buitl int
diffs[3] += 1

print(adapters)

print()
for k,v in diffs.items():
    print(k, v)
print(diffs[1] * diffs[3])

# built in 
# built_in = max() + 3

# not 1560