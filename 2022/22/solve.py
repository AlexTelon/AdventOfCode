from collections import defaultdict
import re
ggrid, instructions = open('in.txt').read().split('\n\n'); SIDE_D = 50

instructions = re.findall(r'\d+[LRN]', instructions.strip()+'N')
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

def pos_to_side(x,y):
    return x // SIDE_D + (y // SIDE_D) * 3

def side_to_pos(side):
    x = side % 3 * SIDE_D
    y = side // 3 * SIDE_D
    return x, y

def rotate_right(dx, dy):
    return -dy, dx

def rotate_left(dx, dy):
    return dy, -dx

X, Y = None, None
facing = dirs['>']

grid = defaultdict(lambda: ' ')
sides = defaultdict(lambda: defaultdict(lambda: ' '))
for y, line in enumerate(ggrid.splitlines()):
    for x, c in enumerate(line):
        side = pos_to_side(x,y)

        if c in '.#':
            grid[(x,y)] = c
            sides[side][(x % SIDE_D, y % SIDE_D)] = c
            if X == None:
                X, Y = x, y


def try_move(x,y, dx,dy):
    dest = grid[(x+dx,y+dy)]
    if dest == '.':
        # Can move so move.
        return (x+dx,y+dy), (dx,dy)
    elif dest == '#':
        # Cant move, move back to original and return that.
        return (x,y), (dx,dy)

    # move around an edge!
    current_side = pos_to_side(x,y)
    face = dirs_to_chr[(dx,dy)]

    xx = x % SIDE_D
    yy = y % SIDE_D

    if current_side == 1:
        if   face == '>': next_side = 2; xx = SIDE_D - 1 - xx
        elif face == '<': next_side = 6; yy = SIDE_D - 1 - yy; face = '>'
        elif face == 'v': next_side = 4; yy = SIDE_D - 1 - yy
        elif face == '^': next_side = 9; xx, yy = yy, xx; face = '>'
    elif current_side == 2:
        if   face == '>': next_side = 7; yy = SIDE_D - 1 - yy; face = '<'
        elif face == '<': next_side = 1; xx = SIDE_D - 1 - xx
        elif face == 'v': next_side = 4; xx, yy = yy, xx; face = '<'
        elif face == '^': next_side = 9; yy = SIDE_D - 1 - yy
    elif current_side == 4:
        if   face == '>': next_side = 2; xx, yy = yy, xx; face = '^'
        elif face == '<': next_side = 6; xx, yy = yy, xx; face = 'v'
        elif face == 'v': next_side = 7; yy = SIDE_D - 1 - yy
        elif face == '^': next_side = 1; yy = SIDE_D - 1 - yy
    elif current_side == 6:
        if   face == '>': next_side = 7; xx = SIDE_D - 1 - xx
        elif face == '<': next_side = 1; yy = SIDE_D - 1 - yy; face = '>'
        elif face == 'v': next_side = 9; yy = SIDE_D - 1 - yy
        elif face == '^': next_side = 4; xx, yy = yy, xx; face = '>'
    elif current_side == 7:
        if   face == '>': next_side = 2; yy = SIDE_D - 1 - yy; face = '<'
        elif face == '<': next_side = 6; xx = SIDE_D - 1 - xx
        elif face == 'v': next_side = 9; xx, yy = yy, xx; face = '<'
        elif face == '^': next_side = 4; yy = SIDE_D - 1 - yy
    elif current_side == 9:
        if   face == '>': next_side = 7; xx, yy = yy, xx; face = '^'
        elif face == '<': next_side = 1; xx, yy = yy, xx; face = 'v'
        elif face == 'v': next_side = 2; yy = SIDE_D - 1 - yy
        elif face == '^': next_side = 6; yy = SIDE_D - 1 - yy
    else:
        assert False

    xx %= SIDE_D
    yy %= SIDE_D

    if sides[next_side][(xx,yy)] == '#':
        # Cant move there so dont move or rotate.
        return (x,y), (dx,dy)
    else:
        # We can move so move.
        x, y = side_to_pos(next_side)
        return (x+xx, y+yy), dirs[face]


path = {}
def debug_draw(all=False):
    def pixel(x,y):
        if (x,y) == (X,Y):
            return "\033[91m" + dirs_to_chr[facing] + "\033[0m"
        if (x,y) in latest:
            return "\033[92m" + latest[(x,y)] + "\033[0m"
        if (x,y) in path:
            return "\033[93m" + path[(x,y)] + "\033[0m"
        if (x,y) in grid:
            c = str(pos_to_side(x,y)) if grid[(x,y)] == '.' else grid[(x,y)]
            if c == '#': return c
            return "\033[90m" + c + "\033[0m"
        return ' '

    width  = max([x for x,y in grid])
    height = max([y for x,y in grid])

    if not all:
        height = min(height, max(y for x,y in latest)+5)

    for y in range(height+1):
        for x in range(width+1):
            print(end=pixel(x,y))
        print()

path[(X,Y)] = dirs_to_chr[facing]
latest = {}

for i, (steps, rot) in enumerate(instructions):
    before = facing

    latest = {}
    for _ in range(steps):
        (X, Y), facing = try_move(X, Y, *facing)
        path[(X,Y)] = dirs_to_chr[facing]
        latest[(X,Y)] = dirs_to_chr[facing]

    if rot == 'R': facing = rotate_right(*facing)
    if rot == 'L': facing = rotate_left(*facing)

debug_draw(all=True)
print(len(instructions))
print(f'final pos {X=} {Y=} {facing=}')

chr_to_score = {
    '^': 3,
    '>': 0,
    'v': 1,
    '<': 2,
}
f = chr_to_score[dirs_to_chr[facing]]
print((Y+1) * 1000 + (X+1) * 4 + f)