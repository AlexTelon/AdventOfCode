from collections import defaultdict
import math
from aocd import submit

grid = defaultdict()
sensors = {}
SENSORS = {}
beacons = set()
distances = []

free = set()

# lines = open('sample.txt').read().splitlines(); MAGIC_ROW = 10
lines = open('in.txt').read().splitlines(); MAGIC_ROW = 2_000_000

def dist(a, b):
    x,y = a
    xx,yy = b

    return abs(xx-x) + abs(yy-y)
    # return math.dist(a,b)


t = 0
for line in lines:
    sensor, nearest_beacon = eval(line)
    grid[sensor] = 'S'
    grid[nearest_beacon] = 'B'

    d = dist(sensor, nearest_beacon)
    print(d, math.dist(sensor, nearest_beacon))

    x,y = sensor
    dist_to_row = dist((x, MAGIC_ROW), sensor)
    # print(dist_to_row, math.dist((x, MAGIC_ROW), sensor))
    if dist_to_row <= d:
        SENSORS[sensor] = ((d - dist_to_row))

    sensors[sensor] = d
    beacons.add(nearest_beacon)

    distances.append(d)

seen = set()
for (x,y), d in SENSORS.items():
    d = int(d)
    derp = range(x-d, x+d+1)
    # for xx in range(x-d, x+d+1):
    #     assert(dist((xx, y), (x,y)) <= d)

    # assert(dist((x-d-1, y), (x,y)) > d)
    # assert(dist((x+d+2, y), (x,y)) > d)

    for x in derp:
        seen.add(x)

    print(derp)

    # seen.append(derp)

# seen = set().union(*seen)

seen -= set(x for x,y in beacons if y == MAGIC_ROW)
print(len(seen))

for x in range(-6, 30):
    if x == 0:
        print(end=str(x))
    if x == 25:
        print(end='v')
    else:
        print(end=' ')
print()
for x in range(-6, 30):
    print(end='#' if x in seen else '.')

# not 5470703
# not 6393843
# not 6920669