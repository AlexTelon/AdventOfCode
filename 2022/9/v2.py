import math

directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

def move_knot(Hx,Hy, Tx,Ty):
    # The basic idea is if they are not touching then move the tail towards head.
    touching = math.dist((Hx,Hy),(Tx,Ty)) < 2
    if not touching:
        # Move tail towards head.
        Ty += [-1, 1][Ty < Hy] if Ty != Hy else 0
        Tx += [-1, 1][Tx < Hx] if Tx != Hx else 0
    return (Tx, Ty)

Hx, Hy = 0, 0
tail = [(0, 0) for _ in range(9)]
seen = set()
for line in open('input.txt').read().splitlines():
    op, d = line.split()
    dx, dy = directions[op]

    for _ in range(int(d)):
        Hx = Hx + dx
        Hy = Hy + dy

        # Move all parts of the tail towards the previous part. Start with H.
        prev = (Hx,Hy)
        tail = [prev := move_knot(*prev, *t) for t in tail]

        seen.add(tail[-1])

print('p2',len(seen))