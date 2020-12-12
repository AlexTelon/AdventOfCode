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

# fractions tips
## Directions
# directions = {
#     '^': (0, 1),
#     'v': (0, -1),
#     '<': (-1, 0),
#     '>': (1, 0),
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
lines = open('input.txt').read().splitlines()
# lines = [ for line in lines]


directions = {
    'N':    (1, 0),
    'E':    (0, 1),
    'S':    (-1, 0),
    'W':    (0, -1),
    'L':    (0, 0, -1),
    'R':    (0, 0, 1),
    'F':    (0, 0, 0),
}
dirs = "NESW"
dir = 'E'
pos = [0, 0]
angle = 90

for line in lines:
    c = line[0]
    vector = directions[c]
    num = int(line[1:])
    if c in 'NESW':
        pos[0] += vector[0] * num
        pos[1] += vector[1] * num
    if c in 'LR':
        assert num in [0, 90, 180, 270]
        num = [0, 90, 180, 270].index(num)
        if c == 'L':
            num = -num
        new_index = (dirs.index(dir) + num) % 4
        old_dir = dir
        dir = dirs[new_index]
        # dir = (dir + vector[2]) % 4
        # print(f'added {num} new angle', angle)
        print(f'{old_dir} -> {dir}', 'num,', num)
    if c == 'F':
        facing_vector = directions[dir]
        print("facing: {dir}", facing_vector)
        pos[0] += facing_vector[0] * num
        pos[1] += facing_vector[1] * num
    print(pos)

print(sum(abs(p) for p in pos))
# not 330