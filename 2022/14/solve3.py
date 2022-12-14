from itertools import pairwise, product
import math

class Grid:
    floor = -math.inf
    start = (500, 0)
    walls = set()
    sand = set()

    def __getitem__(self, pos): 
        if pos[1] == Grid.floor: return '#'
        if pos in Grid.walls:    return '#'
        if pos in Grid.sand:     return 'o'
        if pos == Grid.start:    return 'S'
        return '.'

    def __setitem__(self, pos, value):
        self.sand.add(pos)

    def add_path(self, path):
        for (x,y), (xx,yy) in pairwise(path):
            lo_y = min(y, yy)
            hi_y = max(y, yy)
            lo_x = min(x, xx)
            hi_x = max(x, xx)
            Grid.walls |= {(x,y) for x,y in product(range(lo_x, hi_x+1), range(lo_y, hi_y+1))}
            Grid.floor = max(Grid.floor, lo_y+2)

def sand(current):
    x, y = current
    if   grid[(moved := (x,   y+1))] in '.S': return sand(moved)
    elif grid[(moved := (x-1, y+1))] in '.S': return sand(moved)
    elif grid[(moved := (x+1, y+1))] in '.S': return sand(moved)
    else: return current


grid = Grid()
for line in open('in.txt').read().splitlines():
    grid.add_path([tuple(map(int,x.split(','))) for x in line.split('->')])

while grid[Grid.start] != 'o':
    grid[sand((500, -1))] = 'o'

print(len(Grid.sand))