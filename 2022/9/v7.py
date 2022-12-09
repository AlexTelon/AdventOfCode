import copy
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
    goal = copy.copy(snake[0])
    match op:
        case 'U': goal.y -= int(d)+1
        case 'D': goal.y += int(d)+1
        case 'L': goal.x -= int(d)+1
        case 'R': goal.x += int(d)+1

    while not goal.touching(snake[0]):
        for h,t in pairwise([goal]+snake):
            t.move_towards(h)

        seen.add((t.x, t.y))

print('p2',len(seen))