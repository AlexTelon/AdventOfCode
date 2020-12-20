import math
from collections import defaultdict, Counter
import copy
import itertools
from itertools import product, permutations, combinations, repeat, chain
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

# groups = open(0).read().split("\n\n")
groups = open('input.txt').read().split("\n\n")
# groups = open('sample.txt').read().split("\n\n")
# lines = open(0).read().splitlines()
# # lines = [[int(x) for x in line.split()] for line in lines]
# for line in lines:
#     print(line)

class Grid():
    def __init__(self):
        self.ID = ""
        self.rows = []
        self.r = 0
        self.c = 0

    def __str__(self):
        msg = f"{self.ID}\n"
        for row in self.rows:
            msg += "".join(row) + '\n'
        return msg

    def col(self, c):
        col = []
        for row in self.rows:
            col.append(row[c])
        return col

    def __eq__(self, item):
        return str(self) == str(item)

def flip_v(grid):
    new_rows = copy.copy(grid.rows)

    n = len(grid.rows) - 1
    for y in range(len(grid.rows)):
        new_rows[y] = grid.rows[n - y]
    
    # copy grid
    new_grid = copy.copy(grid)
    new_grid.rows = new_rows
    return new_grid

def flip_h(grid):
    new_rows = copy.deepcopy(grid.rows)

    n = len(grid.rows) - 1
    for y in range(len(grid.rows)):
        for x in range(len(grid.rows)):
            new_rows[y][x] = grid.rows[y][n - x]
        
    # copy grid
    new_grid = copy.copy(grid)
    new_grid.rows = new_rows
    return new_grid

def rotate(grid):
    new_rows = copy.deepcopy(grid.rows)

    n = len(grid.rows) - 1
    for r in range(len(grid.rows)):
        for c in range(len(grid.rows)):
            new_rows[c][n-r] = grid.rows[r][c]
        
    # copy grid
    new_grid = copy.copy(grid)
    new_grid.rows = new_rows
    return new_grid



# if you have multiple lines of stuff in groups, and groups seperated by empty lines.


grids = []

for group in groups:
    grid = Grid()
    for i, line in enumerate(group.splitlines()):
        if i == 0:
            #Tile 2897:
            grid.ID = int(line.split()[-1][:-1])
        else:
            grid.rows.append(list(line))
    grids.append(grid)

# print('FLIP_V')
# print('original', grids[0])
# print('flip_v', flip_v(grids[0]))
# # print('original', grids[0])

# print('FLIP_H')
# print('original', grids[0])
# print('flip_h', flip_h(grids[0]))
# # print('original', grids[0])

# print('rotate')
# print('original', grids[0])
# print('rotate', rotate(grids[0]))
# print('rotate2', rotate(rotate(grids[0])))
# print('rotate3', rotate(rotate(rotate(grids[0]))))
# print('rotate4', rotate(rotate(rotate(rotate(grids[0])))))
# print('original', grids[0])

assert(grids[0] == rotate(rotate(rotate(rotate(grids[0])))))
assert(grids[0] == flip_h(flip_h(grids[0])))
assert(grids[0] == flip_v(flip_v(grids[0])))

def flips(grid):
    yield grid
    yield flip_h(grid)
    yield flip_v(grid)

def rotations(grid):
    tmp = grid
    for _ in range(4):
        yield tmp
        tmp = rotate(tmp)

def variations(grid):
    for flipped in flips(grid):
        for rotated in rotations(flipped):
            yield rotated

assert(len(list(variations(grids[0]))) == 12)

def neighbours(r, c):
    MAX_DIMENSION = 12
    col = c

    for row in range(max(0, r-1), min(MAX_DIMENSION, r+2)):
        if (row, col) == (r, c):
            continue
        yield (row, col)
        
    row = r
    for col in range(max(0, c-1), min(MAX_DIMENSION, c+2)):
        if (row, col) == (r, c):
            continue
        yield (row, col)

assert(set(neighbours(0,0)) == set([(0,1), (1,0)]))
assert(set(neighbours(11,11)) == set([(11,10), (10,11)]))
assert(set(neighbours(5,5)) == set([(5,6), (6,5), (4,5), (5, 4)]))

def get_edge(grid, dir):
    direction = {
        (1, 0):  lambda: grid.rows[-1], # bottom edge (rows goe down)
        (-1, 0): lambda: grid.rows[0],  # top edge
        (0, 1):  lambda: grid.col(-1),  # right edge
        (0, -1): lambda: grid.col(0),   # left edge
        # (0, 1):  lambda: rotate(grid).rows[-1][::-1],   # right edge
        # (0, -1): lambda: rotate(grid).rows[0][::-1],    # left edge
    }
    return direction[dir]()

# print('grid: ', grids[0])
# print("top:", get_edge(grids[0], (-1,0)))
# print("bot:", get_edge(grids[0], (1,0)))
# print("right:", get_edge(grids[0], (0,1)))
# print("left:", get_edge(grids[0], (0,-1)))
# exit()
placement = {}

def is_valid(r,c):
    this = placement[(r,c)]
    for other_pos in neighbours(r,c):
        our_dir = (other_pos[0] - r, other_pos[1] - c)
        their_dir = (-our_dir[0], -our_dir[1])
        our_edge = get_edge(this, our_dir)
        their_edge = get_edge(placement[other_pos], their_dir)
        
        if our_edge != their_edge:
            return False
    return True
# placement[(5,5)] = grids[0]
# placement[(5,6)] = grids[1] # right
# placement[(6,5)] = grids[2] # under
# placement[(5,4)] = grids[3] # left
# placement[(4,5)] = grids[4] # over
# print(is_valid(5,5))

# is_valid(2,2)

def all_possible(grids):
    for grid in grids:
        for this in variations(grid):
            yield this

# def valid_above(this, all):
#     valid = []
#     # (1, 0):  lambda: grid.rows[-1],                 # bottom edge (rows goe down)
#     # (-1, 0): lambda: grid.rows[0],                  # top edge
#     # (0, 1):  lambda: rotate(grid).rows[-1][::-1],   # right edge
#     # (0, -1): lambda: rotate(grid).rows[0][::-1],    # left edge

#     our_dir = (-1, 0)
#     our_edge = get_edge(this, our_dir)
#     their_dir = (-our_dir[0], -our_dir[1])

#     for other in all:
#         their_edge = get_edge(other, their_dir)
#         if our_edge == their_edge:
#             valid.append(other.ID)
    
#     if this.ID in valid:
#         valid.remove(this.ID)

#     return valid

def valid_in_direction(this, all, dir):
    valid = set()
    # (1, 0):  lambda: grid.rows[-1],                 # bottom edge (rows goe down)
    # (-1, 0): lambda: grid.rows[0],                  # top edge
    # (0, 1):  lambda: rotate(grid).rows[-1][::-1],   # right edge
    # (0, -1): lambda: rotate(grid).rows[0][::-1],    # left edge
    our_edge = get_edge(this, dir)
    their_dir = (-dir[0], -dir[1])

    for other in all:
        their_edge = get_edge(other, their_dir)
        if our_edge == their_edge:
            valid.add(other.ID)
    
    if this.ID in valid:
        valid.remove(this.ID)

    return valid

def valid_above(this, all):
    return valid_in_direction(this, all, (-1, 0))

def valid_below(this, all):
    return valid_in_direction(this, all, (1, 0))

def valid_right(this, all):
    return valid_in_direction(this, all, (0, 1))

def valid_left(this, all):
    return valid_in_direction(this, all, (0, -1))

tot = 0
# Corners need only 2 possible neighbours, all other must have 3 or 4. lets hope there are 4 with only 2 possible neighbours
corners = []
stuff = {}
all = list(all_possible(grids))
bottom_right = defaultdict(set)
top_left = defaultdict(set)

# (1, 0): # bottom edge (rows goe down)
# (-1, 0):# top edge
# (0, 1): # right edge
# (0, -1):# left edge
for this in grids:
    for this in variations(this):
        above = valid_above(this,all)
        left = valid_left(this,all)
        right = valid_right(this,all)
        below = valid_below(this,all)
        
        bottom_right[this.ID].update(above)
        bottom_right[this.ID].update(left)

        top_left[this.ID].update(below)
        top_left[this.ID].update(right)


print('bottom_right')
for k,v in bottom_right.items():
    if len(v) == 2:
        print(k,v)

print("top_left")
for k,v in top_left.items():
    if len(v) == 2:
        print(k,v)

print("bottom_left")
for k,v in top_left.items():
    if len(v) == 2:
        print(k,v)
# they have the same keys so I suspect these 4 are our corners
# correct!
print("part1 hack:", math.prod(top_left.keys()))

# print(len(count.keys()))
# for k,v in stuff.items():
#     if len(v) != 0:
#         print(k,v)

# for y in range(12):
#     for x in range(12):
#         for option in variations(grids[y * 12 + x]):
#             print(option)
#             tot += 1
# print(tot)
