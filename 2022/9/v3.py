import math

def touching(x,y, xx,yy):
    return math.dist((x,y),(xx,yy)) < 2

def move_knot(Hx,Hy, Tx,Ty):
    if not touching(Hx,Hy, Tx, Ty):
        Ty += [-1, 1][Ty < Hy] if Ty != Hy else 0
        Tx += [-1, 1][Tx < Hx] if Tx != Hx else 0
    return (Tx, Ty)

Hx, Hy = 0, 0
tail = [(0, 0) for _ in range(9)]
seen = set()
for line in open('input.txt').read().splitlines():
    op, d = line.split()
    d = int(d)
    match op:
        case 'U': dx, dy = ( 0, -1)
        case 'D': dx, dy = ( 0,  1)
        case 'L': dx, dy = (-1,  0)
        case 'R': dx, dy = ( 1,  0)
    
    Hx, Hy = Hx+(dx*d), Hy+(dy*d)
    while not touching(Hx, Hy, *tail[0]):
        prev = Hx, Hy
        tail = [prev := move_knot(*prev, *t) for t in tail]

        seen.add(tail[-1])

print('p2',len(seen))