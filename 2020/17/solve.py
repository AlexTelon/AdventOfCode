from collections import defaultdict
from itertools import count

rows = open(0).read().splitlines()

grid = defaultdict(lambda: '.')

for y, row in enumerate(rows):
    for x, val in enumerate(row):
        grid[(x,y,0,0)] = val


def adjecent(x,y,z,w):
    for i in range(x-1, x+2):
        for j in range(y-1, y+2):
            for k in range(z-1, z+2):
                for l in range(w-1, w+2):
                    if (i,j,k,l) == (x,y,z,w):
                        continue
                    yield (i,j,k,l)

def next_state():
    new_grid = defaultdict(lambda: '.')
    positions = set()
    for pos in grid.keys():
        positions.update(adjecent(*pos))

    for pos in positions:
        value = grid[pos]
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


for i in count(1):
    grid = next_state()
    print(i, sum(val == '#' for val in grid.values()))
    if i >= 6:
        break
print('answer:',sum(val == '#' for val in grid.values()))