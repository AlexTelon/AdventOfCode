from collections import defaultdict
import re
ggrid, instructions = open('in.txt').read().split('\n\n')
# ggrid, instructions = open('sample.txt').read().split('\n\n')
# ggrid, instructions = open('sample2.txt').read().split('\n\n')

instructions = re.findall(r'\d+[LRN]', instructions.strip()
+'N')
instructions = [(steps:=int(inst[:-1]), rot:=inst[-1]) for inst in instructions]

dirs = {
    '^': (0, -1),
    '>': (1, 0),
    'v': (0, 1),
    '<': (-1, 0),
}
dirs_to_chr = {
    (0, -1): '^',
    (1, 0): '>',
    (0, 1): 'v',
    (-1, 0): '<',
}

X, Y = None, None
facing = dirs['>']

grid = defaultdict(lambda: ' ')
for y, line in enumerate(ggrid.splitlines()):
    for x, c in enumerate(line):
        if c in '.#':
            grid[(x,y)] = c

            if X == None:
                X, Y = x, y
    #     print(end=c)
    # print()

def try_move(x,y, dx,dy):
    original = (x,y)

    x += dx
    y += dy

    if (x,y) in grid:
        if grid[(x,y)] == '.':
            return (x,y)
        if grid[(x,y)] == '#':
            # cant move, move back to original and return that.
            return original

    x -= dx
    y -= dy
    # Move in reverse direction until we end up outside, then check again.
    if dy == 0:
        while grid[(x,y)] != ' ':
            x -= dx
    if dx == 0:
        while grid[(x,y)] != ' ':
            y -= dy

    if is_next_wall(x,y,dx,dy):
        return original
    return try_move(x,y, dx, dy)

def is_next_wall(x,y, dx, dy):
    x += dx
    y += dy

    if (x,y) in grid:
        return grid[(x,y)] == '#'


    x -= dx
    y -= dy
    # Move in reverse direction until we end up outside, then check again.
    if dy == 0:
        while grid[(x,y)] != ' ':
            x -= dx
    if dx == 0:
        while grid[(x,y)] != ' ':
            y -= dy

    return is_next_wall(x,y, dx, dy)

print(f'start pos {X=} {Y=} {facing=}')
path = {}

def debug_draw():
    def pixel(x,y):
        if (x,y) in path:
            return path[(x,y)]
        if (x,y) in grid:
            return grid[(x,y)]
        return ' '

    width  = max([x for x,y in grid])
    height = max([y for x,y in grid])

    height2 = max([y for x,y in path]) + 2

    height = min(height, height2)

    for y in range(height):
        for x in range(width):
            print(end=pixel(x,y))
        print()

path[(X,Y)] = dirs_to_chr[facing]
for steps, rot in instructions:
    # Move until we hit a wall!
    dx, dy = facing
    # sign = (dx > 0) - (dx < 0)
    for _ in range(steps):
        X, Y = try_move(X, Y, dx, 0)
        # if is_next_wall(X, Y, dx, 0): continue
        # else: X += dx
        path[(X,Y)] = dirs_to_chr[facing]

    # sign = (dy > 0) - (dy < 0)
    for _ in range(steps):
        X, Y = try_move(X, Y, 0, dy)
        # if is_next_wall(X, Y, 0, dy): continue
        # else: Y += dy
        path[(X,Y)] = dirs_to_chr[facing]

    # Rotate.
    if rot == 'R':
        facing = -facing[1], facing[0]
    if rot == 'L':
        facing = facing[1], -facing[0]

    # debug_draw()
    # print(steps, rot)
    # print(f'final pos {X=} {Y=} {facing=}')
    # if input() == 'q':
    #     quit()

# debug_draw()
print(f'final pos {X=} {Y=} {facing=}')

# ans is 1-indexed
row = (Y+1) * 1000
col = (X+1) * 4

chr_to_score = {
    '^': 3,
    '>': 0,
    'v': 1,
    '<': 2,
}


f = chr_to_score[dirs_to_chr[facing]]
print(dirs_to_chr[facing], f)

print(f"{row} + {col} + {f}")
print(row + col + f)
