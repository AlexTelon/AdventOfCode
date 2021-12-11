from itertools import count
from typing import Tuple, List

class Grid():
    def __init__(self, grid: List[List[int]]):
        self.grid = grid
        assert len(grid) > 0
        self.W = len(grid[0])
        self.H = len(grid)

    @classmethod
    def from_file(cls, filename: str):
        """Constructs a Grid object from file."""
        lines = open(filename).read().splitlines()
        grid = [[int(x) for x in line] for line in lines]
        return cls(grid)

    def inc(self):
        """Increment all values in the grid by 1."""
        for i, line in enumerate(self.grid):
            self.grid[i] = [x+1 for x in line]

    def adjecent(self, x,y):
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
            if x < 0 or x >= self.W or y < 0 or y >= self.H:
                continue
            yield x,y

    def items(self) -> Tuple[Tuple[int,int], int]:
        """Returns an all positions and their values in the grid as tuples."""
        for y, line in enumerate(self.grid):
            for x, value in enumerate(line):
                yield (x,y), value

    def flash(self):
        """Perform all flashes for a step and return the number of flashs performed."""
        flashed = set()

        # Iterate until no more flashes to be done.
        while True:
            len_before = len(flashed)
            for pos, value in self.items():
                if value > 9 and pos not in flashed:
                    flashed.add(pos)

                    # Perform a local flash.
                    for x,y in self.adjecent(*pos):
                        self.grid[y][x] += 1

            if len_before == len(flashed):
                break

        # Reset all flashed lights.
        for x,y in flashed:
            self.grid[y][x] = 0

        return len(flashed)


p1 = 0
grid = Grid.from_file('input.txt')
for i in count(1):
    grid.inc()
    flashes = grid.flash()
    p1 += flashes

    if i == 100:
        print(f"{p1=}")

    if flashes == 100:
        print(f"p2={i}")
        exit()