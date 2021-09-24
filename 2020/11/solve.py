import copy
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
import fileinput


lines = open('input.txt').read().splitlines()
# lines = open('in.sample').read().splitlines()
# lines = [[int(x) for x in line.split()] for line in lines]
# grid = lines
grid = []
for line in lines:
    grid.append([c for c in line])


def print_grid():
    for line in grid:
        print("".join(line))

ROW_MAX = len(grid) - 1
COLUMN_MAX = len(grid[0]) - 1
# grid =

def adjacent(row, column):
    suggestions = [
        (row+1, column), #up
        (row+1, column+1), #diag
        (row+1, column-1), # diag
        (row, column+1), # right
        (row, column-1), # left
        (row-1, column), # down
        (row-1, column+1), # diag
        (row-1, column-1), # diag
    ]
    def clamp(row, column):
        row = max(0, row)
        row = min(ROW_MAX, row)
        column = max(0, column)
        column = min(COLUMN_MAX, column)
        return row, column
    
    adj = set([clamp(*pos) for pos in suggestions])
    #remove self
    if (row, column) in adj:
        adj.remove((row, column))
    return adj
        

def is_occupied2(r,c):
    try:
        return grid[r][c] == "#"
    except IndexError:
        return False

def is_floor2(r,c):
    try:
        return grid[r][c] == "."
    except IndexError:
        return False

def is_empty2(r,c):
    try:
        return grid[r][c] == "L"
    except IndexError:
        return False

def is_occupied(seat):
    return seat == "#"

def is_floor(seat):
    return seat == "."

def is_empty(seat):
    return seat == "L"


def do_iteration(grid):
    changed = False
    # partial would look nice
    for r, row in enumerate(grid):
        for c, seat in enumerate(row):
            # adj = adjacent(r,c)
            debug = [((r,c), is_occupied2(r,c)) for r,c in adjacent(r,c)]

            if (r,c) == (9, 0):
                print('hi')
            # print((r,c), sum(is_occupied2(r,c) for r,c in adjacent(r,c)))
            if is_empty2(r,c) and sum(is_occupied2(r,c) for r,c in adjacent(r,c)) == 0:
                grid[r][c] = '#'
                changed = True
            elif is_occupied2(r,c) and sum(is_occupied2(r,c) for r,c in adjacent(r,c)) >= 4:
                grid[r][c] = 'L'
                changed = True
    return (grid, changed)

changed = True
i = 0
while changed:
    print(i)
    i += 1
    # print_grid()
    tmp_grid = copy.deepcopy(grid)
    grid, changed = do_iteration(tmp_grid)
    # if i > 4:
    #     exit()
print("DONE")

tot = 0
for line in grid:
    tot += sum(is_occupied(seat) for seat in line)
print(tot)
# print(sum(is_occupied(seat) for seat in grid))