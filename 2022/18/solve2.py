from collections import deque
from itertools import combinations, product

def is_adjecent(a, b):
    return sorted(abs(xx-x) for x, xx in zip(a,b)) == [0,0,1]

def surface_area(shape):
    t = len(shape) * 6
    connected = sum([is_adjecent(pos, other) for pos, other in combinations(shape, r=2)])
    return t - connected*2

def adjectens(pos):
    x, y, z = pos
    for dx, dy, dz in product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]):
        if dx == dy == dz == 0: continue
        if not is_adjecent((0,0,0), (dx,dy,dz)): continue
        if x > MAX_X or x < MIN_X: continue
        if y > MAX_Y or y < MIN_Y: continue
        if z > MAX_Z or z < MIN_Z: continue
        yield (x+dx, y+dy, z+dz)


def bfs(start):
    visited = set()
    stack = deque([start])

    while stack:
        current = stack.pop()
        visited.add(current)

        for adj in adjectens(current):
            if adj in shape: continue
            if adj in visited: continue
            stack.append(adj)

    return visited

shape = {tuple(map(int,line.split(','))) for line in open('in.txt').read().splitlines()}

Xs = [x for x,_,_ in shape]
Ys = [y for _,y,_ in shape]
Zs = [z for _,_,z in shape]

MIN_X, MAX_X = min(Xs), max(Xs)
MIN_Y, MAX_Y = min(Ys), max(Ys)
MIN_Z, MAX_Z = min(Zs), max(Zs)

start = (MIN_X, MIN_Y, MIN_Z)
goal  = (MAX_X, MAX_Y, MAX_Z)

visited = bfs(start = start)

volume = {(x,y,z) for x,y,z in product(range(MIN_X, MAX_X+1),range(MIN_Y, MAX_Y+1),range(MIN_Z, MAX_Z+1))}

outside = volume.intersection(visited.union(shape))
inside = volume - outside

p1 = surface_area(shape)
print('p1', p1)
print('part2', p1 - surface_area(inside))