from itertools import pairwise
import math
from aocd import submit

def touching(a, b):
    return math.dist((a.real,a.imag),(b.real,b.imag)) < 2

def move_towards(a, b):
    if not touching(a, b):
        dy = [1, -1][b.imag < a.imag] if b.imag != a.imag else 0
        dx = [1, -1][b.real < a.real] if b.real != a.real else 0
    return a + complex(dx, dy)

# lines = open('in.txt').read().splitlines()
lines = open('sample.txt').read().splitlines()

start = 500 + 0j

MAX_Y = -math.inf
MIN_Y =  math.inf
MAX_X = -math.inf
MIN_X =  math.inf


paths = []
for line in lines:
    points = [complex(*map(int,x.split(','))) for x in line.split('->')]
    for point in points:
        MAX_Y = max(MAX_Y, int(point.imag))
        MIN_Y = min(MIN_Y, int(point.imag))
        MAX_X = max(MAX_X, int(point.real))
        MIN_X = min(MIN_X, int(point.real))
    paths.append(points)

# print(MAX_Y)
# print(MIN_Y)
# print(MAX_X)
# print(MIN_X)
# exit()

grid = {}
grid[start] = 'S'
for path in paths:
    for start, goal in pairwise(path):
        grid[start] = '#'
        grid[goal] = '#'
        current = start
        while not touching(current, goal):
            current = move_towards(current, goal)
            grid[current] = '#'


def print_grid():
    def pixel(x,y):
        if (x,y) == (500, 0):
            return 'S'
        if complex(x,y) in grid:
            return grid[complex(x,y)]
        return '.'

    for y in range(MIN_Y, MAX_Y+1):
        for x in range(MIN_X, MAX_X+1):
            print(end=pixel(x,y))
        print()

print_grid()