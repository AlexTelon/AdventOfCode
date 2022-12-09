from math import dist
from aocd import submit

with open('input.txt', 'r') as f:
# with open('sample.txt', 'r') as f:
    lines = f.read().splitlines()

def print_grid(hx,hy):
    def draw(x,y):
        if (x,y) == (hx, hy):
            return 'H'
        return '#' if (x,y) in seen else '.'
    if seen:
        X = [x for x,y in seen]
        Y = [x for x,y in seen]
        for y in range(min(Y), max(Y)+1):
            print(''.join([draw(x,y) for x in range(min(X), max(X)+1)]))


directions = {
    'U': (0, 1),
    'D': (0, -1),
    'L': (-1, 0),
    'R': (1, 0),
}


Hx, Hy = 0, 0
Tx, Ty = 0, 0
seen = set()
for line in lines:
    op, d = line.split()
    d = int(d)
    dx, dy = directions[op]

    # if op == 'D' and d == 1:
    #     print()
    # print()
    # print(op, d)
    for _ in range(d): 
        Hx = Hx + (dx * 1)
        Hy = Hy + (dy * 1)
        # print('new H', Hx, Hy)

        # if dist((Hx,Hy),(Tx,Ty)) > 1:
        # update Tx
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
        # elif abs(Tx - Hx) >= 1 and abs(Ty - Hy) >= 1:
        elif dist((Hx,Hy),(Tx,Ty)) > 2:
            if Ty > Hy:
                Ty -= 1
            if Ty < Hy:
                Ty += 1
            if Tx > Hx:
                Tx -= 1
            if Tx < Hx:
                Tx += 1

        # print('new T', Tx, Ty)
        seen.add((Tx, Ty))
        # print(seen)
        # print_grid(Hx,Hy)



# print_grid(Hx,Hy)
print(len(seen))