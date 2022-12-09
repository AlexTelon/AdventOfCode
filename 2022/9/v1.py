from math import dist

directions = {
    'U': (0, -1),
    'D': (0, 1),
    'L': (-1, 0),
    'R': (1, 0),
}

def move_knot(Hx,Hy, Tx,Ty):
    if abs(Ty - Hy) > 1 and Tx == Hx:
        Ty += [-1, 1][Ty < Hy]
    elif abs(Tx - Hx) > 1 and Ty == Hy:
        Tx += [-1, 1][Tx < Hx]
    elif dist((Hx,Hy),(Tx,Ty)) > 2:
        Ty += [-1, 1][Ty < Hy]
        Tx += [-1, 1][Tx < Hx]
    return (Tx, Ty)

Hx, Hy = 0, 0
tail = [(0,0) for _ in range(9)]
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