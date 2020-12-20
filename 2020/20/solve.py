import pickle
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
# groups = open('sample2.txt').read().split("\n\n")
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
    }
    return direction[dir]()

# print('grid: ', grids[0])
# print("top:", get_edge(grids[0], (-1,0)))
# print("bot:", get_edge(grids[0], (1,0)))
# print("right:", get_edge(grids[0], (0,1)))
# print("left:", get_edge(grids[0], (0,-1)))
# exit()
placement = {}

# def is_valid(r,c):
#     this = placement[(r,c)]
#     for other_pos in neighbours(r,c):
#         our_dir = (other_pos[0] - r, other_pos[1] - c)
#         their_dir = (-our_dir[0], -our_dir[1])
#         our_edge = get_edge(this, our_dir)
#         their_edge = get_edge(placement[other_pos], their_dir)
        
#         if our_edge != their_edge:
#             return False
#     return True
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

def valid_in_direction(this, all, dir):
    valid = set()
    # (1, 0): # bottom edge (rows goes down)
    # (-1, 0):# top edge
    # (0, 1): # right edge
    # (0, -1):# left edge
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
all_possible = list(all_possible(grids))
bottom_right = defaultdict(set)
top_left = defaultdict(set)

valid_around = defaultdict(dict)

# (1, 0): # bottom edge (rows goe down)
# (-1, 0):# top edge
# (0, 1): # right edge
# (0, -1):# left edge

try:
    with open("pickledump.txt", "rb") as f:
        valid_around = pickle.load(f)
except:
    for this in grids:
        for this in variations(this):
            above = valid_above(this, all_possible)
            left = valid_left(this, all_possible)
            right = valid_right(this, all_possible)
            below = valid_below(this, all_possible)
            
            valid_around[this.ID]['right'] = valid_right(this, all_possible)
            valid_around[this.ID]['left'] = valid_left(this, all_possible)
            valid_around[this.ID]['above'] = valid_above(this, all_possible)
            valid_around[this.ID]['below'] = valid_below(this, all_possible)

    with open("pickledump.txt", "wb") as f:
        pickle.dump(valid_around, f)

# Part2 find the sea monsters
# For this we need to build the full image.
# First lets solve where each grid should be placed

# who references me?
links_to_id = defaultdict(set)
for this_id, valid in valid_around.items():
    for other_id in chain(*valid.values()):
        links_to_id[other_id].add(this_id)

def remove_me(id, others):
    # global links_to_id
    # remove references to id from others
    for other in links_to_id[id]:
        for k, v in valid_around[other].items():
            if id in v:
                valid_around[other][k].remove(id)
    # for _, valid_to in others.items():
    #     for k, v in valid_to.items():
    #         if id in v:
    #             valid_to[k].remove(id)
    # remove id
    del others[id]
    # for k,v in valid_around[id]:
    #     links_to_id[k].remove(id)
    # del links_to_id[id]

def valid_position(pos):
    return all(0 <= p <= 12 for p in pos)

direction_str_to_tuple = {
    'left':  (0, -1),
    'right': (0, 1),
    'below': (1, 0),
    'above': (-1, 0),
}

candidates = deque()
top_left = -1
for id, valid_to in valid_around.items():
    if not any(valid_to['left']):
        if not any(valid_to['above']):
            # top left
            candidates.append(((0,0), id))
        if not any(valid_to['below']):
            # bottom left
            candidates.append(((11,0), id))
    if not any(valid_to['right']):
        if not any(valid_to['above']):
            # top right
            candidates.append(((0,11), id))
        if not any(valid_to['below']):
            # bottom right
            candidates.append(((11,11), id))

# These is a unique solution. 
# So go through all and place the must-have pieces. remove links and then place the new must-have pieces.



current = None
pos = None
placement = {}

# candidates = deque([(pos, current)])
iterations = 0
while any(candidates):
    print()
    print('placements')
    for k,v in placement.items():
        print("     ",k,v)
    iterations += 1

    # find the one with the least number of links to it?
    links = {(pos, candidate):links_to_id[candidate] for pos, candidate in candidates}
    smallest = math.inf
    candidate = None
    for (p, id),v in links.items():
        if len(v) < smallest:
            smallest = len(v)
            pos, current = p, id
    candidates.remove((pos,current))
    print(f"smallest candidate is {pos=} {current=} with len: {smallest}")
        # print(id,v)
    # pos, current = candidates.popleft()
    # print(f'{pos=}, {current=}')
    if pos in placement:
        print('oups', pos)
    placement[pos] = current

    if current == 1511:
        print('now')
        
    print('add candidates')
    for dir, valid in valid_around[current].items():
        if any(valid):
            print(f"    {dir}, {valid} of {pos}")

    for dir, valid in valid_around[current].items():
        if len(valid) == 1:
            candidate = valid.pop()
            diff = direction_str_to_tuple[dir]
            new_pos = (pos[0] + diff[0], pos[1] + diff[1])
            if valid_position(new_pos):
                if new_pos in placement:
                    print(f'dont add {candidate}: {pos} + {diff} == {new_pos}')
                else:
                    print(f'adding ({new_pos}, {candidate})')
                    candidates.append((new_pos, candidate))
        

    remove_me(current, valid_around)
    links_to_id = defaultdict(set)
    for this_id, valid in valid_around.items():
        for other_id in chain(*valid.values()):
            links_to_id[other_id].add(this_id)

    # print('batman count', links_to_id[2999])
    assert not any(links_to_id[current])
    # for k,v in links_to_id.items():
    #     if len(v) == 2:
    #         print(f'next one should be {k}:{v}')
    print(f'candidate: {candidates}')



print('iterations: ', iterations)
print('left: ', len(valid_around))
print('placed: ', len(placement))
print(placement)
# start with top left. it has no valid to 