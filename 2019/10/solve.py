from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat
from computer import Computer
import queue
from threading import Thread
from collections import deque
from decimal import Decimal

asteroids = []

data = [line.strip() for line in open('input.txt')]

W = 10
H = 10

for y, line in enumerate(data):
    # print(y, line)
    for x, item in enumerate(line):
        # print(x, item)
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
# a = (-3, 0)
# # b = (0, -2)
# b = (-1, -2)
# print(is_divisible_by(a, b))
# print('hi')
# exit()
# def is_divisible(a , b):

#     # if not (a[0] < 0 and b[0] < 0 or a[0] > 0 and b[0] > 0):
#     #     return False
#     # if not (a[1] < 0 and b[1] < 0 or a[1] > 0 and b[1] > 0):
#     #     return False


#     if a == (-1, 0) and b == (1, 0):
#         print('hi')

#     if b[0] == 0:
#         if a[1] % b[1] == 0:
#             if a[1] > 0 and b[1] < 0 or a[1] < 0 and b[1] > 0:
#                 return False
#             return a[0] == 0
#         return False
        
#     if b[1] == 0:
#         if a[0] % b[0] == 0:
#             if a[0] > 0 and b[0] < 0 or a[0] < 0 and b[0] > 0:
#                 return False
#             return a[1] == 0
#         return False

#     # if b[0] == 0:
#     #     if a[1] % b[1] == 0:
#     #         return a[0] == 0
#     #     return False

#     # if b[1] == 0:
#     #     if a[0] % b[0] == 0:
#     #         return a[1] == 0
#     #     return False

#     # if 0 in b:
#     #     if a[0] == b[0] or a[1] == b[1]:
#     #         return True
#     #     return False
#     # if b[0] == 0 or b[1] == 0:
#     #     return True

#     derp1 = a[0] % b[0] == 0
#     derp2 = a[1] % b[1] == 0

#     derp = a[0] % b[0] == 0 and a[1] % b[1] == 0
#     return derp

def seen_from(x, y):
    total = 0
    seen_slopes = set()
    # if x == 4 and y == 0:
    #     print('hi')
    for i, j in asteroids:
        if i == x and j == y:
            continue


        slope = ((x - i), (y - j))
        least = min(abs(slope[0]), abs(slope[1]))
        
        # make it (0, 1) or (0, -1) so we keep the sign
        if slope[0] == 0:
            slope = (0, slope[1] // abs(slope[1]))
        if slope[1] == 0:
            slope = (slope[0] // abs(slope[0]), 0)

        # make the slope as small as possible
        if least not in [0, 1]:
            if slope[0] % least == 0 and slope[1] % least == 0:
                slope = (slope[0] // least, slope[1] // least)

        #     # slope = (Decimal(slope[0] / least), Decimal(slope[1] / least))

        # if you can build one slope with any other then dont add it?

        seen_slopes.add(slope)


        # print(slope, least)
        # if i == x or j == y:
        #     total += 1
        
        # # combinations of 
        # # -width - 0 - width
        # # -height - 0 - height
        # # so (1,3) means move 1 to right, then 3 up. But do so step by step so that we dont jump over anything

        # for x_step in range(-W, W):
        #     for y_step in range(-H, H):

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

            # if is_divisible(slope, other):
            #     # Then dont add it
            #     break
            # otherwise add it
            # print(f"Adding {slope}")
            result.add(slope)
            break

    # # result = {slope for slope in seen_slopes if not any(is_divisible(slope, other) for other in seen_slopes if slope !=)}
    return result
    # return len(seen_slopes)


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
# index = seen.index(value)
pprint(seen)
pprint(f"best is results[{index}]: {stuff[index]}")
print()
print(f"Best {value}")

# print("\n".join(seen))

# 333 is too high
# 332 is too high (just guessed in case I was off-by-one)