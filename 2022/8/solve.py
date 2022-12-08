from functools import partial
import math

with open('input.txt') as f:
    lines = f.read().splitlines()

grid = []
for y, row in enumerate(lines):
    grid.append(list(map(int,row)))

cols = list(zip(*grid))

def views(x,y):
    """Returns the view in the 4 directions from a given position.
    The order is defined as in aoc. above, left, right, below

    Also they are ordered as seen from the (x,y) coordinate.
    """
    above = cols[x][:y]
    left  = grid[y][:x]
    right = grid[y][x+1:]
    below = cols[x][y+1:]
    return [above[::-1], left[::-1], right, below]

def direction_score(house, direction):
    """The score for the given direction"""
    t = 0
    for num in direction:
        t += 1
        if num >= house:
            break
    return t

p1 = 0
p2 = 0
for y, row in enumerate(grid):
    for x, house in enumerate(row):
        if any(house > max(other or [-math.inf]) for other in views(x,y)):
            p1 += 1
        dir_score = partial(direction_score, house)
        score = math.prod(map(dir_score, views(x,y)))
        if score > p2:
            p2 = score

print('p1',p1)
print('p2',p2)