from itertools import pairwise
import math

def touching(a, b):
    return math.dist((a.real,a.imag),(b.real,b.imag)) < 2

def move_towards(a, b):
    if not touching(a, b):
        dy = [1, -1][b.imag < a.imag] if b.imag != a.imag else 0
        dx = [1, -1][b.real < a.real] if b.real != a.real else 0
    return a + complex(dx, dy)

lines = open('in.txt').read().splitlines()

start = 500 + 0j

MAX_Y = -math.inf
MIN_Y =  math.inf
MAX_X = -math.inf
MIN_X =  math.inf

def update_bounds(pos):
    global MAX_Y, MIN_Y, MAX_X, MIN_X
    MAX_Y = max(MAX_Y, int(pos.imag))
    MIN_Y = min(MIN_Y, int(pos.imag))
    MAX_X = max(MAX_X, int(pos.real))
    MIN_X = min(MIN_X, int(pos.real))


paths = []
for line in lines:
    points = [complex(*map(int,x.split(','))) for x in line.split('->')]
    paths.append(points)
    for pos in points:
        update_bounds(pos)

paths.append([complex(MIN_X-1000,MAX_Y+2), complex(MAX_X+1000,MAX_Y+2)])

update_bounds(paths[-1][0])
update_bounds(paths[-1][1])
update_bounds(start)

grid = {}
grid[start] = 'S'
for path in paths:
    for a, goal in pairwise(path):
        grid[a] = '#'
        grid[goal] = '#'
        current = a
        while not touching(current, goal):
            current = move_towards(current, goal)
            grid[current] = '#'

def print_grid(viz):
    def pixel(x,y):
        if complex(x,y) in grid:
            return grid[complex(x,y)]
        if complex(x,y) in viz:
            return viz[complex(x,y)]
        if (x,y) == (500, 0):
            return 'S'
        return '.'

    for y in range(MIN_Y, MAX_Y+1):
        for x in range(MIN_X, MAX_X+1):
            print(end=pixel(x,y))
        print()

def simulate_sand(pos):
    viz = {}
    # goal is always down.
    down = 1j
    # if blocked try these
    down_left  = -1 + 1j
    down_right = 1 + 1j

    current = pos
    while True:
        stopped = True
        for delta in [down, down_left, down_right]:
            candidate = current + delta

            air = candidate not in grid or candidate == start
            if air:
                # move through air.
                # viz[candidate] = '~'
                current = candidate
                stopped = False
                break
            else:
                continue
        if stopped:
            break
        # # p1
        # if current.imag > MAX_Y:
        #     print(sum(v == 'o' for v in grid.values()))
        #     quit()
        # p2
        if grid[500 + 0j] == 'o':
            print(sum(v == 'o' for v in grid.values()))
            quit()
    grid[current] = 'o'
    return viz

while True:
    viz = simulate_sand(start-1j)
    # print_grid(viz)
    # if input() in ['q', 'quit']:
    #     quit()