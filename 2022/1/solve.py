from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat, count
import queue
from collections import deque
from decimal import Decimal
from fractions import Fraction
import fractions
# import networkx
import string
import operator
import re


with open('input.txt', 'r') as f:
    groups = f.read().split('\n\n')

# data = [tuple(map(int, line.strip().split('x'))) for line in lines]
# nums = re.findall(r'-?\d+', 'a12b13')

x, y   = 0,0
dx, dy = 0,0
t = 0
# p1
print(max(sum(int(line) for line in g.splitlines()) for g in groups))
# p2
print(sum(sorted([sum(int(line) for line in g.splitlines()) for g in groups])[-3:]))