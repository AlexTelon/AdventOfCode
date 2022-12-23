from collections import defaultdict
from itertools import count, cycle
MIN_X, MAX_X, MIN_Y, MAX_Y = 0,0,0,0

lines = open('in.txt').read().splitlines()
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


elfs = set()
for y, line in enumerate(lines):
    for x, c in enumerate(line):
        if c == '#':
            elfs.add((x,y))


def update_bounds():
    global MIN_X, MAX_X, MIN_Y, MAX_Y
    MIN_X = min(x for x,_ in elfs)
    MAX_X = max(x for x,_ in elfs)
    MIN_Y = min(y for _,y in elfs)
    MAX_Y = max(y for _,y in elfs)

def lone_elf(x,y):
    for (xx, yy) in directions.values():
        if (x+xx, y+yy) in elfs:
            return False
    return True

def elf(x,y):
    return (x,y) in elfs

def no_elf_in(dirs):
    for d in dirs:
        xx, yy = directions[d]
        if (x+xx, y+yy) in elfs:
            return False
    return True

rules = cycle([
    (['N', 'NE', 'NW'], 'N'),
    (['S', 'SE', 'SW'], 'S'),
    (['W', 'NW', 'SW'], 'W'),
    (['E', 'NE', 'SE'], 'E'),
])

update_bounds()


for i in count(1):
    out_grid = defaultdict(list)

    # prep phase.
    MOVED = False
    # for y in range(MIN_Y, MAX_Y+1):
    #     for x in range(MIN_X, MAX_X+1):
            # if not elf(x,y): continue
    for x,y in elfs:
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
                MOVED = True
        if not moved:
            out_grid[(x, y)].append((x,y))
    
    if not MOVED:
        break

    new_elfs = set()
    for pos, candidates in out_grid.items():
        if len(candidates) == 1:
            # Move it.
            new_elfs.add(pos)
        else:
            # dont let them move.
            for c in candidates:
                new_elfs.add(c)

    elfs = new_elfs

    # move phase.
    update_bounds()

    next(rules)


print('part2', i)