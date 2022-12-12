from collections import defaultdict, deque
import math
import string

letters = string.ascii_lowercase
def height(c):
    if c == 'S':
        c = 'a'
    elif c == 'E':
        c = 'z'
    return letters.index(c)

assert height('a') == 0
assert height('S') == height('a')
assert height('E') == height('z')

def valid_h_diff(start,stop):
    return height(stop) - height(start) <= 1

assert valid_h_diff('a', 'b') == True
assert valid_h_diff('b', 'a') == True
assert valid_h_diff('z', 'a') == True
assert valid_h_diff('a', 'c') == False

def can_move(start, stop):
    if stop not in ggrid:
        return False
    a = ggrid[start]
    b = ggrid[stop]
    return valid_h_diff(a,b)

directions = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0),
}

def print_grid(grid):
    for row in grid:
        print(row)

def adjecent(x,y):
    for a,b in [(x-1,y), (x+1,y), (x,y-1), (x,y+1)]:
        if (a,b) in ggrid:
            yield (a,b)

def debug_print():
    def pixel(x,y):
        d = dist[(x,y)]
        if d < math.inf:
            return f"{d:02}"
        return '  '
    for y,row in enumerate(grid):
        print(' '.join([pixel(x,y) for x, c in enumerate(row)]))

lines = open('input.txt').read().splitlines()

grid = [row for y, row in enumerate(lines)]
ggrid = {}

start = 0, 0
goal  = 0, 0
for y,row in enumerate(grid):
    for x, c in enumerate(row):
        ggrid[(x,y)] = c
        if c == 'S':
            start = (x,y)
        elif c == 'E':
            goal = (x,y)

dist = defaultdict(lambda:math.inf)
dist[goal] = 0

current = goal
que = deque()
visited = set()
i = 0

done = [False, False]
p2 = None
while not all(done):
    i += 1
    visited.add(current)
    for adj in adjecent(*current):
        if can_move(adj, current) and adj not in visited:
            dist[adj] = min(dist[adj], dist[current]+1)
            if adj not in visited and adj not in que:
                que.append(adj)
    current = que.popleft()

    if current == start:
        done[0] = True
    if ggrid[current] == 'a':
        if p2 == None:
            p2 = dist[current]
        done[1] = True
    # if i % 10 == 0:
    #     debug_print()
    #     input()

print('p1', dist[start])
print('p2', p2)
