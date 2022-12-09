from dataclasses import dataclass
import math

@dataclass
class Point:
    x: int
    y: int

def touching(a, b):
    return math.dist((a.x, a.y), (b.x, b.y)) < 2

def move_knot(H, T):
    if not touching(H, T):
        T.y += [-1, 1][T.y < H.y] if T.y != H.y else 0
        T.x += [-1, 1][T.x < H.x] if T.x != H.x else 0
    return T

H = Point(0, 0)
tail = [Point(0, 0) for _ in range(9)]
seen = set()
for line in open('input.txt').read().splitlines():
    op, d = line.split()
    match op:
        case 'U': H.y -= int(d)
        case 'D': H.y += int(d)
        case 'L': H.x -= int(d)
        case 'R': H.x += int(d)

    while not touching(H, tail[0]):
        prev = H
        tail = [prev := move_knot(prev, t) for t in tail]

        T = tail[-1]
        seen.add((T.x, T.y))

print('p2',len(seen))