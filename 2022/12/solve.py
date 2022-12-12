from collections import defaultdict, deque
import math
import string

letters = string.ascii_lowercase + string.ascii_uppercase
def height(c):
    return letters.index(c.replace('S','a').replace('E','z'))

def can_move(start, stop):
    return height(grid[stop]) - height(grid[start]) <= 1

directions = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0),
}

def adjecent(x,y):
    yield from [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]

lines = open('input.txt').read().splitlines()

# Outside is 'Z' and is too high to climb.
grid = defaultdict(lambda: 'Z')

start = None
goal  = None
for y,row in enumerate(lines):
    for x, c in enumerate(row):
        grid[(x,y)] = c
        if c == 'S': start = (x,y)
        elif c == 'E': goal = (x,y)

dist = defaultdict(lambda:math.inf)
dist[goal] = 0

que = deque([goal])
visited = set()

p1 = None
p2 = None
while not (p1 and p2):
    current = que.popleft()
    visited.add(current)
    for adj in adjecent(*current):
        if can_move(adj, current):
            dist[adj] = min(dist[adj], dist[current]+1)
            if adj not in visited and adj not in que:
                que.append(adj)

    if current == start:
        p1 = dist[current]
    if grid[current] == 'a':
        if p2 == None:
            p2 = dist[current]

print('p1', dist[start])
print('p2', p2)