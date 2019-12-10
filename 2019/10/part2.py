
import pickle
import operator
import math

with open('part1.pickle', 'rb') as handle:
    stuff = pickle.load(handle)


# from the ideal position (25, 31) use the slopes there
origin = (25, 31)
slopes = list(stuff[origin])
# have been thinking y is up, but y is down..
# slopes = [(slope[0], -slope[1]) for slope in slopes]
# data = open('result.txt').read()


with open('part1_small.pickle', 'rb') as handle:
    stuff = pickle.load(handle)
# origin = (11, 13)
data = open('result_small.txt').read()
slopes = eval(data)
# l = len(slopes)


def clockwise(slope):
    radians = math.atan2(slope[1], slope[0]) + math.pi / 2
    # hack to get the last quadrant too come last (it has negative angle)
    if radians < 0:
        radians += 4 * math.pi
    return radians


# print(clockwise((0, -1)))
# print(clockwise((1, 0)))
# print(clockwise((0, 1)))
# print(clockwise((-1, 0)))
# print(clockwise((-10, -1)))
# exit()

def possible_positions(slope):
    x_min = 0
    x_max = 100
    if slope[0] < 0:
        x_max = -x_max
    
    y_min = 0
    y_max = 100
    if slope[1] < 0:
        y_max = -y_max

    if slope[0] == 0:
        x = 0
        for y in range(y_min, y_max, slope[1]):
            yield (x,y)
        return

    if slope[1] == 0:
        y = 0
        for x in range(x_min, x_max, slope[0]):
            yield (x,y)
        return

    for x, y in zip(range(x_min, x_max, slope[0]), range(y_min, y_max, slope[1])):
        yield (x,y)


import itertools

print(f"origin {origin}")

removed = 0
# need a function to sort them in clockwise order
for i, slope in enumerate(itertools.cycle(sorted(slopes, key = lambda slope: clockwise(slope)))):
# for i, slope in enumerate(sorted(slopes, key = lambda slope: clockwise(slope))):
    # print(i, len(stuff))
    # print(f'slope {slope}', end=" ")
    for shift in possible_positions(slope):
        if shift == (0, 0):
            continue
        pos = (origin[0] + shift[0], origin[1] + shift[1])
        # print(f'pos: {pos}')
        if pos in stuff:
            removed += 1
            print(f'{removed} removed is!: {pos}')
            if removed == 200:
                print(pos)
                print("result: ", (pos[0] * 100) + pos[1])
                exit()
            del stuff[pos]
            break

