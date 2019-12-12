from collections import defaultdict, Counter, namedtuple
import itertools
from itertools import product, permutations, combinations, repeat
# from computer import Computer
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

    def __hash__(self):
        tmp = (hash(self.pos), hash(self.velocity))
        return hash(tmp)


# io = Moon(Position(x=1, y=4, z=4))
# europa = Moon(Position(x=-4, y=-1, z=19))
# ganymede = Moon(Position(x=-15, y=-14, z=12))
# callisto = Moon(Position(x=-17, y=1, z=10))

# example
io = Moon(Position(x=-1, y=0, z=2))
europa = Moon(Position(x=2, y=-10, z=-7))
ganymede = Moon(Position(x=4, y=-8, z=8))
callisto = Moon(Position(x=3, y=5, z=-1))

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

hashes = {}
moon_saving = []
moon_saving.append({})
moon_saving.append({})
moon_saving.append({})
moon_saving.append({})

cycles_found_for = set()
eqvations = []
result_tuples = []

def check_state(step):
    """Works but didnt read the thing about us needing to find a more efficient way to do this."""
    # moon = moons[1]
    # new = tuple(hash(moon) for moon in moons)
    for i, moon in enumerate(moons):
        new = hash((moon.pos, moon.velocity))
        if new in moon_saving[i]:
            if i in cycles_found_for:
                continue
            cycles_found_for.add(i)
            constant = moon_saving[i][new]
            cycle = step - constant
            # print()
            # print(f"found cycle for {i}")
            # print(f"state: {moon}")
            # print(f"previously found at step: {moon_saving[i][new]}, now at step {step}: cycle: {step - moon_saving[i][new]}")
            print(f"{i}: {constant} + {cycle}x")
            eqvations.append(f"{constant} + {cycle}{'xyzp'[i]}")
            result_tuples.append((constant, cycle))

            if len(cycles_found_for) == 4:
                print("done found all needed solutions!")
                print(" = ".join(eqvations))
                print("cycle: ", ", ".join(str(cycle) for constant, cycle in result_tuples))
                exit()

        else:
            moon_saving[i][new] = step

# pprint(moons)
for step in itertools.count():
    check_state(step)
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

# loop for [0]:
# [Position(x=1, y=4, z=4)>, Velocity(x=0, y=0, z=0),
#  Position(x=-4, y=-1, z=19)>, Velocity(x=0, y=0, z=0),
#  Position(x=-15, y=-14, z=12)>, Velocity(x=0, y=0, z=0),
#  Position(x=-17, y=1, z=10)>, Velocity(x=0, y=0, z=0)]
# found one!
# previously found at step: 11078743
# state: pos=<Position(x=150, y=656, z=-293)>, vel=<Velocity(x=-50, y=1, z=-26)>
# current step: 11187087
# diff: 108344


# [Position(x=1, y=4, z=4)>, Velocity(x=0, y=0, z=0),
#  Position(x=-4, y=-1, z=19)>, Velocity(x=0, y=0, z=0),
#  Position(x=-15, y=-14, z=12)>, Velocity(x=0, y=0, z=0),
#  Position(x=-17, y=1, z=10)>, Velocity(x=0, y=0, z=0)]
# found one!
# previously found at step: 2447170
# state: pos=<Position(x=-186, y=-293, z=-636)>, vel=<Velocity(x=34, y=-3, z=-59)>
# current step: 4614050
# diff: 2166880


# [Position(x=1, y=4, z=4)>, Velocity(x=0, y=0, z=0),
#  Position(x=-4, y=-1, z=19)>, Velocity(x=0, y=0, z=0),
#  Position(x=-15, y=-14, z=12)>, Velocity(x=0, y=0, z=0),
#  Position(x=-17, y=1, z=10)>, Velocity(x=0, y=0, z=0)]
# found one!
# previously found at step: 4672896
# state: pos=<Position(x=80, y=69, z=-136)>, vel=<Velocity(x=-6, y=4, z=-6)>
# current step: 5372626
# diff: 699730

# [Position(x=1, y=4, z=4)>, Velocity(x=0, y=0, z=0),
#  Position(x=-4, y=-1, z=19)>, Velocity(x=0, y=0, z=0),
#  Position(x=-15, y=-14, z=12)>, Velocity(x=0, y=0, z=0),
#  Position(x=-17, y=1, z=10)>, Velocity(x=0, y=0, z=0)]
# found one!
# previously found at step: 828902
# state: pos=<Position(x=753, y=342, z=-210)>, vel=<Velocity(x=45, y=-10, z=11)>
# current step: 15153058
# diff: 14324156


eqvations = []
# start, cycle
(11078743, 108344) # 11078743 + 108344x
(2447170, 2166880) # 2447170 + 2166880x
(4672896, 699730) # 4672896 + 699730x
(828902, 14324156) # 828902 + 14324156x

# 0 x20 = 1
# 1 -> 2 

# loop over all and find each planets possible cycles.
# every time a new cycle is found add it and check if a common cycle can be found