from dataclasses import dataclass
from itertools import pairwise
import math

@dataclass
class Point:
    x: int
    y: int

    def touching(self, other):
        return math.dist((self.x, self.y), (other.x, other.y)) < 2
    
    def move_towards(self, other):
        if not self.touching(other):
            self.y += [-1, 1][self.y < other.y] if self.y != other.y else 0
            self.x += [-1, 1][self.x < other.x] if self.x != other.x else 0

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

    while not H.touching(tail[0]):
        for h,t in pairwise([H]+tail):
            t.move_towards(h)

        seen.add((t.x, t.y))

print('p2',len(seen))