from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat, count
import queue
from threading import Thread
from collections import deque
from decimal import Decimal
from fractions import Fraction
import fractions
# import networkx
import string
import operator

# fractions tips
## Directions
# directions = {
#     '^': (0, 1),
#     'v': (0, -1),
#     '<': (-1, 0),
#     '>': (1, 0),
# }
# directions = {
#     'north':    (1, 0),
#     'east':     (0, 1),
#     'south':    (0, -1),
#     'west':     (-1, 0),
# }
# dirs = [directions[c] for line in open('input.txt') for c in line]

## Alphabet
# alphas = string.ascii_lowercase 

# op_codes = {
#     'AND': operator.and_,
#     'OR' : operator.or_,
#     'RSHIFT' : operator.rshift,
#     'NOT' : lambda a,b: not b
# }

# product('ABCD', repeat=2)                 -> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                   -> AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                   -> AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)  -> AA AB AC AD BB BC BD CC CD DD

#data = [tuple(map(int, line.strip().split('x'))) for line in open('input.txt')]

# if you have multiple lines of stuff in groups, and groups seperated by empty lines.
# groups = open(0).read().split("\n\n")
# for group in groups:
#     for line in group.splitlines():
#         print(line)

## read file line by line
# some code that reads a file line by line
# lines = open('input.txt').read().splitlines()
lines = open(0).read().splitlines()
lines = [[int(x) for x in line.split()] for line in lines]
for line in lines:
    print(line)
