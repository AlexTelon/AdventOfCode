from collections import defaultdict
from itertools import cycle
import math
MIN_X, MAX_X, MIN_Y, MAX_Y = 0,0,0,0

lines = open('in.txt').read().splitlines()
# lines = open('sample.txt').read().splitlines()
# lines = open('sample2.txt').read().splitlines()

directions = {
    'N':    (0, -1),
    'E':    (1, 0),
    'NE':   (1, -1),
    'NW':   (-1, -1),

    'S':    (0, 1),
    'W':    (-1, 0),
    'SW':   (-1, 1),
    'SE':   (1, 1),
}


grid = defaultdict(lambda: '.')
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        grid[(x,y)] = c


def update_bounds():
    global MIN_X, MAX_X, MIN_Y, MAX_Y
    MIN_X = min(x for x,_ in grid)
    MAX_X = max(x for x,_ in grid)
    MIN_Y = min(y for _,y in grid)
    MAX_Y = max(y for _,y in grid)

def lone_elf(x,y):
    for (xx, yy) in directions.values():
        if grid[(x+xx, y+yy)] == '#':
            return False
    return True

def elf(x,y):
    return grid[(x, y)] == '#'

def no_elf_in(dirs):
    for d in dirs:
        xx, yy = directions[d]
        if grid[(x+xx, y+yy)] == '#':
            return False
    return True

def debug_draw():
    for y in range(MIN_Y, MAX_Y+1):
        for x in range(MIN_X, MAX_X+1):
            print(end=grid[(x,y)])
        print()

rules = cycle([
    (['N', 'NE', 'NW'], 'N'),
    (['S', 'SE', 'SW'], 'S'),
    (['W', 'NW', 'SW'], 'W'),
    (['E', 'NE', 'SE'], 'E'),
])

update_bounds()
print('initial state')
debug_draw()
print()


for i in range(10):
    out_grid = defaultdict(list)

    # prep phase.
    for y in range(MIN_Y, MAX_Y+1):
        for x in range(MIN_X, MAX_X+1):
            if not elf(x,y): continue
            if lone_elf(x,y):
                out_grid[(x, y)].append((x,y))
                continue

            moved = False
            for _ in range(4):
                dirs, move = next(rules)
                
                if no_elf_in(dirs) and not moved:
                    xx, yy = directions[move]
                    out_grid[(x+xx, y+yy)].append((x,y))
                    moved = True
                    print((x,y), move, 'to ', x+xx, y+yy)
            if not moved:
                print((x,y), 'found nowhere to move')
                out_grid[(x, y)].append((x,y))
    print()

    new_grid = defaultdict(lambda: '.')
    for pos, candidates in out_grid.items():
        if len(candidates) == 1:
            # Move it.
            new_grid[pos] = '#'
        else:
            # dont let them move.
            for c in candidates:
                new_grid[c] = '#'

    grid = new_grid
    # print(len(grid))

    # move phase.
    update_bounds()
    debug_draw()
    # if input() == 'q': quit()

    next(rules)




t = 0
for y in range(MIN_Y, MAX_Y+1):
    for x in range(MIN_X, MAX_X+1):
        t += grid[(x,y)] == '.'
print(t)

# not 5538
# not 4569
# not 4443