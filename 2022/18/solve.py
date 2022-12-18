from collections import deque
from itertools import combinations, product

lines = open('in.txt').read().splitlines()
# lines = open('sample.txt').read().splitlines()
# lines = """1,1,1
# 1,1,2
# 1,1,4
# 1,1,5
# """.splitlines()

def is_adjecent(a, b):
    diffs = []
    for x, xx in zip(a,b):
        diffs.append(abs(xx-x))
    return sorted(diffs) == [0,0,1]

def surface_area(shape):
    t = len(shape) * 6
    connected = 0
    for pos, other in combinations(shape, r=2):
        if pos == other: continue
        connected += is_adjecent(pos, other)
    return t- connected*2

shape = set()
for line in lines:
    x,y,z = map(int,line.split(','))
    shape.add((x,y,z))

print('p1', surface_area(shape))

def adjectens(pos):
    x, y, z = pos

    for dx, dy, dz in product([-1, 0, 1], [-1, 0, 1], [-1, 0, 1]):
        if dx == dy == dz == 0: continue
        if not is_adjecent(pos, (x+dx,y+dy,z+dz)): continue
        if x > MAX_X or x < MIN_X: continue
        if y > MAX_Y or y < MIN_Y: continue
        if z > MAX_Z or z < MIN_Z: continue
        yield (x+dx, y+dy, z+dz)


def bfs(start, goal):
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

Xs = [x for x,_,_ in shape]
Ys = [y for _,y,_ in shape]
Zs = [z for _,_,z in shape]

MIN_X, MAX_X = min(Xs), max(Xs)
MIN_Y, MAX_Y = min(Ys), max(Ys)
MIN_Z, MAX_Z = min(Zs), max(Zs)

start = (MIN_X, MIN_Y, MIN_Z)
goal  = (MAX_X, MAX_Y, MAX_Z)

# print(f"{start=}")
# print(f"{goal=}")

visited = bfs(start = start, goal=goal)

assert not visited.intersection(shape)

x_diff = MAX_X - MIN_X + 1 + 2
y_diff = MAX_Y - MIN_Y + 1 + 2
z_diff = MAX_Z - MIN_Z + 1 + 2

# print(f"{x_diff=}, {MIN_X}, {MAX_X}")
# print(f"{y_diff=}")
# print(f"{z_diff=}")
# volume = {(x,y,z) for x,y,z in product(range(MIN_X, MAX_X+1),range(MIN_Y, MAX_Y+1),range(MIN_Z, MAX_Z+1))}
# assert len(volume) == x_diff * y_diff * z_diff

volume = {(x,y,z) for x,y,z in product(range(MIN_X, MAX_X+1),range(MIN_Y, MAX_Y+1),range(MIN_Z, MAX_Z+1))}

# print('volume', len(volume))
# print('visited:', len(visited))
# print('shape', len(shape))
# print('diff', volume.intersection(shape))

outside = volume.intersection(visited.union(shape))

def pixel(x,y,z):
    if   (x,y,z) in visited:print(end='.')
    elif (x,y,z) in shape:  print(end='#')
    else: print(end='_')

def pixel2(x,y,z):
    # if     (x,y,z) == start: print(end="s")
    # 
    if   (x,y,z) in outside:print(end='#')
    else: print(end='_')

def print_stuff():
    for z in range(MIN_Z-1, MAX_Z+2):
        print(f"{z=}")
        for y in range(MIN_Y-1, MAX_Y+2):
            for x in range(MIN_X-1, MAX_X+2):
                pixel2(x,y,z)
            print()

inside = volume - outside
# print(inside)
# print(len(inside))
print('part2', surface_area(shape) - surface_area(inside))