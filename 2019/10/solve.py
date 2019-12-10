from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat
import queue
from threading import Thread
from collections import deque
from decimal import Decimal
from fractions import Fraction
import fractions

asteroids = []

data = [line.strip() for line in open('input.txt')]

for y, line in enumerate(data):
    for x, item in enumerate(line):
        if item == '#':
            asteroids.append((x,y))

def is_divisible_by(a , b):
    # check if we by repeating b can build a
    if b[0] == 0 and b[1] == 0:
        return a[0] == 0 and b[0] == 0

    x_min = 0
    x_max = 100
    if b[0] < 0:
        x_max = -x_max
    
    y_min = 0
    y_max = 100
    if b[1] < 0:
        y_max = -y_max


    if b[0] == 0:
        x = 0
        for y in range(y_min, y_max, b[1]):
            if a == (x, y):
                return True
        return False

    if b[1] == 0:
        y = 0
        for x in range(x_min, x_max, b[0]):
            if a == (x, y):
                return True
        return False

    for x, y in zip(range(x_min, x_max, b[0]), range(y_min, y_max, b[1])):
        if a == (x, y):
            return True

    return False



def seen_from(x, y):
    total = 0
    seen_slopes = set()
    # if x == 4 and y == 0:
    #     print('hi')
    for i, j in asteroids:
        if i == x and j == y:
            continue

        other = (i, j)
        origin = (x, y)

        # slope = ((x - i), (y - j))
        slope = ((i - x), (j - y))
        least = abs(fractions.gcd(*slope))
        
        # make it (0, 1) or (0, -1) so we keep the sign
        if slope[0] == 0:
            slope = (0, slope[1] // abs(slope[1]))
        if slope[1] == 0:
            slope = (slope[0] // abs(slope[0]), 0)

        if least not in [0, 1]:
            if slope[0] % least == 0 and slope[1] % least == 0:
                slope = (slope[0] // least, slope[1] // least)


        # if slope == (-24, -1):
        #     print('here')

        seen_slopes.add(slope)

    result = set()
    # for slope in seen_slopes:
    for slope in sorted(seen_slopes, key = lambda x: abs(x[0]) + abs(x[1])):
        if len(result) == 0:
            result.add(slope)
        # print(f"Adding {slope}")

        for other in result:
            if slope == other:
                break

            if any(is_divisible_by(slope, other) for other in result):
                # print(f"{slope} is_divisible_by one of {result}")
                break                

            result.add(slope)
            break

    return result

# derp = seen_from(25, 31)
# print(25, 31)
# print(derp)
# with open('result.txt', 'w') as f:
#     a = ",".join(str(x) for x in derp)
#     f.write(a)
# exit()


# How many can be seen
seen = {}
stuff = {}

for asteroid in asteroids:
    # print(asteroid)
    # print()
    can_see = seen_from(*asteroid)
    seen[asteroid] = len(can_see)
    stuff[asteroid] = can_see

# print("\n".join(data))
# print(asteroids)

from pprint import pprint
# pprint(seen)
for y, line in enumerate(data):
    for x, item in enumerate(line):
        if (x,y) in seen:
            print(seen[(x,y)], end="")
        else:
            print(".", end="")
    print()

import operator
value = max(seen.values())
index = max(seen, key=seen.get)
pprint(seen)
pprint(f"best is results[{index}]: {stuff[index]}")
print()
print(f"Best {value}")


with open('result_small.txt', 'w') as f:
    a = ",".join(str(x) for x in stuff[index])
    f.write(a)

import pickle
with open('part1_small.pickle', 'wb') as handle:
    pickle.dump(stuff, handle, protocol=pickle.HIGHEST_PROTOCOL)

# with open('part1.pickle', 'rb') as handle:
#     b = pickle.load(handle)

# print(stuff == b)

# # part2
# # from the ideal position (25, 31) use the slopes there
# data = open('result.txt').read()
# slopes = eval(data)