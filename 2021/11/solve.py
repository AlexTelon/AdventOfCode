grid = open('input.txt').read().splitlines()
grid = [[int(x) for x in line] for line in grid]
W = 10
H = 10

def inc(grid):
    for i, line in enumerate(grid):
        grid[i] = [x+1 for x in line]

def adjecent(x,y):
    yield x, y+1
    yield x, y-1
    yield x+1, y
    yield x-1, y

    yield x+1, y+1
    yield x-1, y-1
    yield x+1, y-1
    yield x-1, y+1

def flash(grid):
    flashed_already = set()
    while True:
        len_before = len(flashed_already)
        for y, line in enumerate(grid):
            for x, c in enumerate(line):
                if c > 9 and (x,y) not in flashed_already:
                    flashed_already.add((x,y))
                    for i,j in adjecent(x,y):
                        if i < 0 or i >= W or j < 0 or j >= H:
                            continue
                        grid[j][i] += 1

        if len_before == len(flashed_already):
            break

    for x,y in flashed_already:
        grid[y][x] = 0

    return len(flashed_already)

p1 = 0
i = 0
while True:
    i += 1
    inc(grid)
    flashes = flash(grid)
    if i == 101:
        print(f"{p1=}")
    if flashes == 100:
        print(f"p2={i}")
        exit()
    p1 += flashes