from itertools import count
from typing import Tuple

grid = open('input.txt').read().splitlines()
grid = [[int(x) for x in line] for line in grid]
W = 10
H = 10

def inc(grid) -> None:
    """Increment all values in the grid by 1."""
    for i, line in enumerate(grid):
        grid[i] = [x+1 for x in line]

def adjecent(x,y):
    """Return all valid adjecent positions."""
    positions = [
        (x, y+1),
        (x, y-1),
        (x+1, y),
        (x-1, y),
        (x+1, y+1),
        (x-1, y-1),
        (x+1, y-1),
        (x-1, y+1)
    ]

    for x,y in positions:
        if x < 0 or x >= W or y < 0 or y >= H:
            continue
        yield x,y


def iter_grid(grid) -> Tuple[Tuple[int,int], int]:
    """Returns an all positions and their values in the grid as tuples."""
    for y, line in enumerate(grid):
        for x, value in enumerate(line):
            yield (x,y), value


def flash(grid):
    """Perform all flashes for a step and return the number of flashs performed."""
    flashed = set()

    # Iterate until no more flashes to be done.
    while True:
        len_before = len(flashed)
        for pos, value in iter_grid(grid):
            if value > 9 and pos not in flashed:
                flashed.add(pos)

                # Perform a local flash.
                for x,y in adjecent(*pos):
                    grid[y][x] += 1

        if len_before == len(flashed):
            break

    # Reset all flashed lights.
    for x,y in flashed:
        grid[y][x] = 0

    return len(flashed)

p1 = 0
for i in count(1):
    inc(grid)
    flashes = flash(grid)
    p1 += flashes

    if i == 100:
        print(f"{p1=}")

    if flashes == 100:
        print(f"p2={i}")
        exit()