from collections import deque
import math

grid = open('input.txt').read().splitlines()
W = len(grid[0])
H = len(grid)

def adjacent(x,y):
    yield x+1, y
    yield x, y+1
    yield x-1, y
    yield x, y-1

def get(grid, pos):
    x,y = pos
    if y < 0 or y >= H:
        return math.inf
    if x < 0 or x >= W:
        return math.inf
    return int(grid[y][x])

lowpoints = {}
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        around = [get(grid, pos) for pos in adjacent(x,y)]
        c = int(c)
        if all(c < x for x in around):
            lowpoints[(x,y)] = c

print('p1', sum(lowpoints.values()) + len(lowpoints))

def bfs(grid, root):
    que = deque()
    seen = set()

    seen.add(root)
    que.append(root)

    while que:
        current_pos = que.popleft()
        current_height = get(grid, current_pos)
        for pos in adjacent(*current_pos):
            if pos not in seen:
                height = get(grid, pos)
                # height 9 cannot ever be included.
                if height < 9 and height > current_height:
                    seen.add(pos)
                    que.append(pos)
    return seen

# find the basins around each lowpoint by doing bfs search around it.
sizes = sorted([len(bfs(grid, (x,y))) for (x,y), value in lowpoints.items()])
print('p2', math.prod(sizes[-3:]))