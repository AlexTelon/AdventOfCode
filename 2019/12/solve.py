from collections import defaultdict, Counter, namedtuple
import itertools
from itertools import product, permutations, combinations, repeat
from computer import Computer
import queue
from threading import Thread
from collections import deque
from decimal import Decimal
import operator
from pprint import pprint

# Moons: Io, Europa, Ganymede, and Callisto.

Position = namedtuple('Position', ['x', 'y', 'z'])
Velocity = namedtuple('Velocity', ['x', 'y', 'z'])
# Moon = namedtuple('Moon', ['pos', 'velocity'])

class Moon():
    def __init__(self, pos):
        self.pos = pos
        self.velocity = Velocity(x=0, y=0, z=0)

    def __str__(self):
        # pos=<x=-1, y=  0, z= 2>, vel=<x= 0, y= 0, z= 0>
        return f"pos=<{self.pos}>, vel=<{self.velocity}>"
    
    def __repr__(self):
        # pos=<x=-1, y=  0, z= 2>, vel=<x= 0, y= 0, z= 0>
        return f"{self.pos}>, {self.velocity}"
        # return f"pos=<{self.pos}>, vel=<{self.velocity}>"


io = Moon(Position(x=1, y=4, z=4))
europa = Moon(Position(x=-4, y=-1, z=19))
ganymede = Moon(Position(x=-15, y=-14, z=12))
callisto = Moon(Position(x=-17, y=1, z=10))

# example
# io = Moon(Position(x=-1, y=0, z=2))
# europa = Moon(Position(x=2, y=-10, z=-7))
# ganymede = Moon(Position(x=4, y=-8, z=8))
# callisto = Moon(Position(x=3, y=5, z=-1))

moons = []
moons.extend([io, europa, ganymede, callisto])

def update_positions():
    def pull(ax, bx):
        if ax > bx:
            return -1
        elif ax == bx:
            return 0
        return 1

    def get_new_velocity(a, b):
        x = pull(a.pos.x, b.pos.x) + a.velocity.x
        y = pull(a.pos.y, b.pos.y) + a.velocity.y
        z = pull(a.pos.z, b.pos.z) + a.velocity.z

        return Velocity(x, y, z)

    for a, b in combinations(moons, 2):
        # print(a, b)
        a.velocity = get_new_velocity(a, b)
        b.velocity = get_new_velocity(b, a)


def update_velocities():
    def get_new_pos(a):
        x = a.pos.x + a.velocity.x
        y = a.pos.y + a.velocity.y
        z = a.pos.z + a.velocity.z

        return Position(x, y, z)

    for moon in moons:
        moon.pos = get_new_pos(moon)

pprint(moons)
for step in range(0, 1000):
    update_positions()
    update_velocities()
    
    # print(f"step: {step+1}")
    # pprint(moons)

print("end")
print(f"step: {step}")
pprint(moons)

total = 0
for moon in moons:
    pot = sum(abs(n) for n in moon.pos)
    kin = sum(abs(v) for v in moon.velocity)
    print(f"{pot} {kin}")
    total += pot * kin

print(f"energy: {total}")

# 12036000 is wrong

# def get_data():
#     lines = [line.strip() for line in open('input.txt')]
#     lines = [line[1:-2] for line in lines]
#     data = [line.strip().split(',') for line in lines]
#     data = [x.split('=') for d in data for x in d]
#     data = [(x[0], int(x[1])) for x in data]

#     return data
#     <x=1, y=4, z=4>
# <x=-4, y=-1, z=19>
# <x=-15, y=-14, z=12>
# <x=-17, y=1, z=10>

# data = get_data()
# print(data)
# exit()