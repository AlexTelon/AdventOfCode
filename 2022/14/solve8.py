from time import perf_counter
t1_start = perf_counter()
from collections import deque
from itertools import pairwise, product

wall = set()
for line in open('in.txt').read().splitlines():
    for (x,y), (xx,yy) in pairwise(tuple(map(int,x.split(','))) for x in line.split('->')):
        wall |= set(product(range(min(x,xx), max(x,xx)+1), range(min(y,yy), max(y,yy)+1)))

floor = max(y for _, y in wall) + 2
sand = set()

def air(pos):
    return pos not in sand and pos not in wall and pos[1] != floor

path = deque([(500, -1)])
pos = (500, 0)
while path:
    x,y = pos
    if   air(new := (x,   y+1)): path.append(pos); pos = new
    elif air(new := (x-1, y+1)): path.append(pos); pos = new
    elif air(new := (x+1, y+1)): path.append(pos); pos = new
    else:
        sand.add(pos)
        if pos == (500, 0):
            print(len(sand))
            break

        pos = path.pop()

t1_stop = perf_counter()
print("Elapsed time during the whole program in seconds:", t1_stop-t1_start)