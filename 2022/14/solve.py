from collections import defaultdict
from itertools import pairwise
import math

def move_towards(a, b):
    sign_y = (a.imag < b.imag) - (a.imag > b.imag)
    sign_x = (a.real < b.real) - (a.real > b.real)
    return a + complex(sign_x, sign_y)

lines = open('in.txt').read().splitlines()

START = 500 + 0j

FLOOR = -math.inf
MAX_X = -math.inf
MIN_X =  math.inf

def update_bounds(pos):
    global FLOOR, MAX_X, MIN_X
    # FLOOR is 2 below everything else.
    FLOOR = max(FLOOR, int(pos.imag)+2)
    MAX_X = max(MAX_X, int(pos.real))
    MIN_X = min(MIN_X, int(pos.real))

def calc_path(path):
    for x in path:
        update_bounds(x)
    for current, goal in pairwise(path):
        grid[current] = '#'
        while current != goal:
            current = move_towards(current, goal)
            grid[current] = '#'

grid = defaultdict(lambda:'.')
grid[START] = 'S'
for line in lines:
    calc_path([complex(*map(int,x.split(','))) for x in line.split('->')])

# Add a floor.
calc_path([complex(MIN_X-1000, FLOOR), complex(MAX_X+1000, FLOOR)])

def simulate_sand(current):
    down = 1j
    down_left  = -1 + 1j
    down_right = 1 + 1j

    moved = True
    while moved:
        moved = False
        for delta in [down, down_left, down_right]:
            candidate = current + delta
            if grid[candidate] in '.S':
                current = candidate
                moved = True
                break
            continue
    grid[current] = 'o'

while True:
    simulate_sand(START-1j)
    # End simulation once the sand reached the start.
    if grid[START] == 'o':
        print(sum(v == 'o' for v in grid.values()))
        quit()