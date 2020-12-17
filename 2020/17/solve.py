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
# product('ABCD', repeat=2)                 -> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                   -> AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                   -> AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)  -> AA AB AC AD BB BC BD CC CD DD

rows = open(0).read().splitlines()
# lines = [(line, i+1) for i, line in enumerate(lines)]
# lines = [[int(x) for x in line.split()] for line in lines]
# for line in rows:
#     print(line)

x,y,z = 0,0,0

def adjecent(x,y,z):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                if (i,j,k) == (x,y,z):
                    continue
                yield (i,j,k)

grid = defaultdict(lambda: '.')

for y, row in enumerate(rows):
    for x, val in enumerate(row):
        grid[(x,y,0)] = val

def next_state():
    new_grid = defaultdict(lambda: '.')
    positions = set()
    for pos in grid.keys():
        positions.update(adjecent(*pos))

    for pos in positions:
        value = grid[pos]
        # print(pos, value)
        new = '-1'
        if value == "#":
            if len([a for a in adjecent(*pos) if grid[a] == '#']) in [2,3]:
                new = '#'
            else:
                new = '.'
        if value == ".":
            if len([a for a in adjecent(*pos) if grid[a] == '#']) in [3]:
                new = '#'
            else:
                new = '.'
        new_grid[(pos)] = new
    return new_grid


for i in count(0):
    grid = next_state()
    print(i)
    # print(grid)
    # for z in range(-1, 2):
    #     print()
    #     print(f'z={z}')
    #     for y, row in enumerate(rows):
    #         print()
    #         for x, val in enumerate(row):
    #             print(grid[(x,y,z)], end="")
    #     # for pos, value in grid.items():
    #     #     i,j,k = pos
    #     #     if k == z:
    #     #         print(value, end="")
    print(i, sum(val == '#' for val in grid.values()))

    # if i >= 1:
    #     break
    if i >= 5:
        break
print(sum(val == '#' for val in grid.values()))


# print(len([a for a in adjecent(0,0,0)]))