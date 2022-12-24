from collections import defaultdict, deque

grid = open('in.txt').read().splitlines()
# grid = open('example.txt').read().splitlines()
# grid = open('sample.txt').read().splitlines()

blizzards = defaultdict(list)

X,Y = None, None
gx,gy = None, len(grid) - 1
HEIGHT = len(grid)
WIDTH = len(grid[0])
ggrid = {}
walls = set()
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        if c in '><v^':
            blizzards[(x,y)].append(c)
            ggrid[(x,y)] = '.'
        else:
            ggrid[(x,y)] = c

        if c == '#':
            walls.add((x,y))

        if c == '.':
            if y == 0 and X == None:
                X,Y = x,y

for x, c in enumerate(grid[-1]):
    if c == '.':
        gx = x
        break


directions = {
    '>': (1, 0),
    '<': (-1, 0),
    'v': (0, 1),
    '^': (0, -1),
}


# print('start', X, Y)
# print('goal', gx, gy)

def debug_draw(state, pos=None, path=None):
    if pos is None:
        pos = (X,Y)
    for y, line in enumerate(grid):
        for x, c in enumerate(line):
            # if (x,y) == (X,Y):
            #     print(end='E')
            if (x,y) == pos:
                print(end='E')
            elif (x,y) in path:
                c = 'p'
                red ='\N{ESC}[31m'
                green ='\N{ESC}[32m'
                if len(state[(x,y)]) > 0:
                    print(end=red + c + '\u001b[0m')
                else:
                    print(end=green + c + '\u001b[0m')
            elif (x,y) in walls:
                print(end='#')
            elif (x,y) in state:
                stuff = state[(x,y)]
                if len(stuff) == 0:
                    print(end='.')
                elif len(stuff) == 1:
                    print(end=stuff[0])
                else:
                    print(end=str(len(stuff)))
            else:
                print(end=ggrid[(x,y)])
        print()
    print()

def next_state(prev_state):
    new_blizzards = defaultdict(list)
    for pos, kinds in prev_state.items():
        for kind in kinds:
            dx, dy = directions[kind]
            x, y = pos
            x += dx
            y += dy

            if grid[y][x] == '#':
                if dx == 0 and dy == 1: # down
                    y = 1
                if dx == 0 and dy == -1: # up
                    y = HEIGHT - 2
                if dy == 0 and dx == 1: # right
                    x = 1
                if dy == 0 and dx == -1: # left
                    x = WIDTH - 2

            new_blizzards[(x,y)].append(kind)
    
    return new_blizzards


_states = [0]*10000
_states[0] = blizzards
def states(time):
    if _states[time] == 0:
        _states[time] = next_state(_states[time-1])
    return _states[time]

move_name = {
    (0,  0): 'S',
    (1,  0): 'R',
    (-1, 0): 'L',
    (0,  1): 'D',
    (0, -1): 'U',
}

que = deque([(X,Y,0,[])])
seen = set()
time = 0
while que:
    x,y,time,path = que.popleft()
    if (x,y,time) in seen: continue
    seen.add((x,y,time))
    state = states(time)

    if (x,y) == (gx, gy) and sum(path) == 2:
        print('part2',time)
        break
    elif len(state[(x,y)]) == 0 and (x,y) not in walls and x >= 0 and y >= 0 and x < WIDTH and y < HEIGHT:
        # up, down, left, right, stand still
        for dx,dy in [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]:
            new_pos = x+dx, y+dy
            if (x,y) == (gx, gy) and sum(path) == 0:
                que = deque([(*new_pos, time+1, path + [True])])
                print('part1', time)
            elif (x,y) == (X, Y) and sum(path) == 1:
                que = deque([(*new_pos, time+1, path + [True])])
            else:
                que.append((*new_pos, time+1, path))
