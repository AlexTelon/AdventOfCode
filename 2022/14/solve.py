from collections import UserDict, defaultdict
from itertools import pairwise
import math

START = 500 + 0j
FLOOR = -math.inf

def move_towards(a, b):
    sign_y = (a.imag < b.imag) - (a.imag > b.imag)
    sign_x = (a.real < b.real) - (a.real > b.real)
    return a + complex(sign_x, sign_y)

class Grid(UserDict):
    verticals = defaultdict(set)
    horizontals = defaultdict(set)

    def __getitem__(self, pos): 
        if any(lo <= pos.imag <= hi for lo,hi in Grid.verticals[pos.real]):   return '#'
        if any(lo <= pos.real <= hi for lo,hi in Grid.horizontals[pos.imag]): return '#'
        # if pos.imag == max(Grid.horizontals.keys())+2: return '#'
        return self.data.get(pos, '.')

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



for line in open('in.txt').read().splitlines():
# for line in open('sample.txt').read().splitlines():
    points = [complex(*map(int,x.split(','))) for x in line.split('->')]
    for a,b in pairwise(points):
        if a.real == b.real:
            lo = min(a.imag, b.imag)
            hi = max(a.imag, b.imag)
            Grid.verticals[int(a.real)].add((lo,hi))
        else:
            lo = min(a.real, b.real)
            hi = max(a.real, b.real)
            Grid.horizontals[int(a.imag)].add((lo, hi))
Grid.horizontals[max(Grid.horizontals)+2].add((-math.inf, math.inf))

def print_grid():
    for y in range(0, FLOOR+1):
        for x in range(490, 510+1):
            print(end=grid[complex(x,y)])
        print()

grid = Grid({START:'S'})
while grid[START] != 'o':
    simulate_sand(START-1j)
    # print_grid()
    # if input() == 'q':
    #     quit()
print(sum(v == 'o' for v in grid.values()))