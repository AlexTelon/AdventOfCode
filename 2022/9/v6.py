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

snake = [Point(0, 0) for _ in range(10)]
seen = set()
for op, d in map(str.split,open('input.txt').read().splitlines()):
    H = snake[0]
    match op:
        case 'U': H.y -= int(d)
        case 'D': H.y += int(d)
        case 'L': H.x -= int(d)
        case 'R': H.x += int(d)

    while not H.touching(snake[1]):
        for h,t in pairwise(snake):
            t.move_towards(h)

        seen.add((t.x, t.y))

print('p2',len(seen))