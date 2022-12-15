from collections import defaultdict
from itertools import pairwise
import math

grid = defaultdict()
SENSORS = {}
beacons = set()

free = set()

lines = open('sample.txt').read().splitlines(); MAGIC_ROW = 10; MAX_DIM = 20
# lines = open('in.txt').read().splitlines(); MAGIC_ROW = 2_000_000; MAX_DIM = 4_000_000

def dist(a, b):
    x,y = a
    xx,yy = b
    return abs(xx-x) + abs(yy-y)


t = 0
for line in lines:
    sensor, nearest_beacon = eval(line)
    grid[sensor] = 'S'
    grid[nearest_beacon] = 'B'

    d = dist(sensor, nearest_beacon)

    x,y = sensor
    SENSORS[sensor] = d

    beacons.add(nearest_beacon)


# for y in range(3349000, MAX_DIM+1):
for y in range(0, MAX_DIM+1):
    if y % 1000 == 0:
        print(y, f"{y/MAX_DIM:%}")
    # seen = set()
    # row = set(range(0, MAX_DIM+1))
    ranges = []
    # scanned = set()
    for (sx, sy), d in SENSORS.items():
        dy = abs(sy - y)
        if d > dy:
            dx = d - dy
            ranges.append((max(0,sx-dx), min(MAX_DIM+1, sx+dx+1)))

    ranges.append((MAX_DIM, MAX_DIM+10))

    ranges = sorted(ranges)
    LO = ranges[0][0]
    if LO > 0:
        print('found it! lo', LO, y)
        exit()
    HI = 0
    for (lo,hi), (lo2, hi2) in pairwise(ranges):
        HI = max(HI, hi)
        if HI < lo2:
            print('found it! hi', HI, y)
            exit()


    # found it! 3418492 3349056

    # not 11448721143552

    # missing = row - scanned
    # if missing:
    #     print(missing, y)
    #     exit()
    continue
    for x in range(0, MAX_DIM+1):
        print(end='#' if x in scanned else '.')
        # if (x,y) == (14, 11):print(end='X')
        # else:print(end='#' if x in row else '.')
    print()
    # seen |= set(x for x,y in beacons if y)
    # # print(*set(range(0, MAX_X+1)))
    # # print(*seen)
    # # print()

    # free = set(range(0, MAX_DIM+1)) - seen
    # if any(row):
    #     print(row, y)

    # if min(seen) > 0 or max(seen) < 20:
    # print(len(seen))

# for x in range(-6, 30):
#     if x == 0:
#         print(end=str(x))
#     if x == 25:
#         print(end='v')
#     else:
#         print(end=' ')
# print()
# for x in range(-6, 30):
#     print(end='#' if x in seen else '.')