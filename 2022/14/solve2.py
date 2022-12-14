from collections import UserDict
from itertools import pairwise, product
import math

class Grid(UserDict):
    floor = -math.inf

    def __getitem__(self, pos): 
        if pos[1] == Grid.floor: return '#'
        return self.data.get(pos, '.')

    def add_path(self, path):
        for (x,y), (xx,yy) in pairwise(path):
            lo_y = min(y, yy)
            hi_y = max(y, yy)
            lo_x = min(x, xx)
            hi_x = max(x, xx)
            self |= {(x,y):'#' for x,y in product(range(lo_x, hi_x+1), range(lo_y, hi_y+1))}

            Grid.floor = max(Grid.floor, lo_y+2)

START = (500, 0)
grid = Grid({START: 'S'})
for line in open('in.txt').read().splitlines():
    grid.add_path([tuple(map(int,x.split(','))) for x in line.split('->')])

while grid[START] != 'o':
    x, y = (500, -1)
    if   grid[(current := (x,   y+1))] in '.S': grid[current] = 'o'
    elif grid[(current := (x-1, y+1))] in '.S': grid[current] = 'o'
    elif grid[(current := (x+1, y+1))] in '.S': grid[current] = 'o'
print(sum(v == 'o' for v in grid.values()))