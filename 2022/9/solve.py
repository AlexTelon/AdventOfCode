from itertools import pairwise
from math import dist

with open('input.txt', 'r') as f:
# with open('sample.txt', 'r') as f:
# with open('larger_example.txt', 'r') as f:
    lines = f.read().splitlines()

def print_grid(hx,hy, tail):
    def draw(x,y):
        if (x,y) == (0, 0):
            return 's'
        if (x,y) == (hx, hy):
            return 'H'
        for i, pos in enumerate(tail, start=1):
            if (x,y) == pos:
                return str(i)
        return '#' if (x,y) in seen else '.'

    if seen:
        X = [x for x,_ in seen | set(tail) | {(hx,hy)}]
        Y = [y for _,y in seen | set(tail) | {(hx,hy)}]

        lines = []
        for y in range(min(Y), max(Y)+1):
            lines.append(''.join([draw(x,y) for x in range(min(X), max(X)+1)]))

        for line in lines[::-1]:
            print(line)


directions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}

def move_knot(Hx,Hy, Tx, Ty):
    if abs(Ty - Hy) > 1 and Tx == Hx:
        if Ty > Hy:
            Ty -= 1
        if Ty < Hy:
            Ty += 1
    elif abs(Tx - Hx) > 1 and Ty == Hy :
        if Tx > Hx:
            Tx -= 1
        if Tx < Hx:
            Tx += 1
    elif dist((Hx,Hy),(Tx,Ty)) > 2:
        if Ty > Hy:
            Ty -= 1
        if Ty < Hy:
            Ty += 1
        if Tx > Hx:
            Tx -= 1
        if Tx < Hx:
            Tx += 1
    return (Tx, Ty)

Hx, Hy = 0, 0
tail = [(0,0) for _ in range(9)]
seen = set()
for line in lines:
    op, d = line.split()
    d = int(d)
    dx, dy = directions[op]

    # print()
    # print('===', op, d, '===')
    # print()
    for _ in range(d): 
        Hx = Hx + (dx * 1)
        Hy = Hy + (dy * 1)

        # Move all parts of the tail towards the previous part. Start with H.
        prev = (Hx,Hy)
        new_tail = []
        for t in tail:
            prev = move_knot(*prev, *t)
            new_tail.append(prev)

        # Update with the new tail.
        tail = new_tail
        seen.add(tail[-1])
    # print()
    # print_grid(Hx,Hy, tail=tail)
    # if input() in ['q', 'quit']:
    #     quit()


# print()
print_grid(Hx,Hy, tail=tail)
print('p2',len(seen))