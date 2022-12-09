from dataclasses import dataclass
from itertools import pairwise
import math
from typing import List

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

    def __mul__(self, i: int):
        return Point(self.x * i, self.y * i)
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

snake = [Point(0, 0) for _ in range(10)]
seen = set()
goals: List[Point] = []

# First generate all goals that the snake will move towards!
# Note that each goal here is one step too far since the Head will always
# stop one step away from the goal.
pos = Point(0,0)
for op, d in map(str.split,open('input.txt').read().splitlines()):
    match op:
        case 'U': delta = Point(0, -1)
        case 'D': delta = Point(0, 1)
        case 'L': delta = Point(-1, 0)
        case 'R': delta = Point(1, 0)
    # Keep track of our true position.
    pos = pos + (delta * int(d))
    # But the snake's goal is alwasy one extra step away such that the Head ends up at pos.
    goals.append(pos + delta)

# We have now seperated the moving of the snake from the gathering of the goals.
# Can be useful!
for goal in goals:
    while not goal.touching(snake[0]):
        for h,t in pairwise([goal]+snake):
            t.move_towards(h)
        seen.add((t.x, t.y))

print('p2',len(seen))