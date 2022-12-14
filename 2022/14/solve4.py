from itertools import pairwise, product
import math

FLOOR = -math.inf
START = (500, 0)
WALLS = set()
SAND  = set()

def get(pos): 
    if pos[1] == FLOOR: return '#'
    if pos in WALLS:    return '#'
    if pos in SAND:     return 'o'
    if pos == START:    return 'S'
    return '.'

def add_path(path):
    global WALLS, FLOOR
    for (x,y), (xx,yy) in pairwise(path):
        lo_y = min(y, yy)
        hi_y = max(y, yy)
        lo_x = min(x, xx)
        hi_x = max(x, xx)
        WALLS |= {(x,y) for x,y in product(range(lo_x, hi_x+1), range(lo_y, hi_y+1))}
        FLOOR = max(FLOOR, lo_y+2)

def sand(current):
    x, y = current
    if   get(moved := (x,   y+1)) in '.S': return sand(moved)
    elif get(moved := (x-1, y+1)) in '.S': return sand(moved)
    elif get(moved := (x+1, y+1)) in '.S': return sand(moved)
    else: return current


for line in open('in.txt').read().splitlines():
    add_path([tuple(map(int,x.split(','))) for x in line.split('->')])

while START not in SAND:
    SAND.add(sand((500, -1)))

print(len(SAND))