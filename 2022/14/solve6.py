from itertools import pairwise, product

block = set()
for line in open('in.txt').read().splitlines():
    for (x,y), (xx,yy) in pairwise(tuple(map(int,x.split(','))) for x in line.split('->')):
        block |= set(product(range(min(x,xx), max(x,xx)+1), range(min(y,yy), max(y,yy)+1)))

floor = max(y for _,y in block)
walls = len(block)

def air(pos): return pos[1] != floor+2 and pos not in block

def flow(x,y):
    if   air(moved := (x,   y+1)): return flow(*moved)
    elif air(moved := (x-1, y+1)): return flow(*moved)
    elif air(moved := (x+1, y+1)): return flow(*moved)
    return x,y

while (500, 0) not in block:
    block.add(flow(500, -1))

print(len(block) - walls)