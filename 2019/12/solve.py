import itertools
from collections import defaultdict, namedtuple
from itertools import combinations
from functools import reduce
from math import gcd


Position = namedtuple('Position', ['x', 'y', 'z'])
Velocity = namedtuple('Velocity', ['x', 'y', 'z'])

class Moon():
    def __init__(self, pos):
        self.pos = pos
        self.velocity = Velocity(x=0, y=0, z=0)
    
    def __repr__(self):
        return f"{self.pos}>, {self.velocity}"

    def __hash__(self):
        tmp = (hash(self.pos), hash(self.velocity))
        return hash(tmp)


io = Moon(Position(x=1, y=4, z=4))
europa = Moon(Position(x=-4, y=-1, z=19))
ganymede = Moon(Position(x=-15, y=-14, z=12))
callisto = Moon(Position(x=-17, y=1, z=10))

# example 1
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


def lcm_iter(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)


origin_positions = [moon.pos for moon in moons]
# [(x1, x2, x3), (y1, y2, y3), (z1, z2, z3)]
origin = list(zip(*origin_positions))
# cycles for x, y and z
cycles = {}


def check_state(step):
    # We will get back to the initial state.
    # Once we do we have found the shortest (and only) cycle time.

    # Since x, y and z changes are independent we can calculate the smallest loop for each
    # Then we can later on use the individual (independent) cycles to find the first time the cycles all happen at the same time.
    # This is done with LCM. Least Common Multiple.
    positions = [moon.pos for moon in moons]
    for i, prop in enumerate(zip(*positions)):
        if prop == origin[i]:
            if step == 0:
                continue
            if i not in cycles:
                cycles[i] = step + 1


for step in itertools.count():
    check_state(step)

    if len(cycles) == 3:
        print(cycles.values())
        print("Part 2: ", lcm_iter(cycles.values()))
        exit()

    update_positions()
    update_velocities()


# Part 1 below. comment out the part 2 exit code above to get to here.
total = 0
for moon in moons:
    pot = sum(abs(n) for n in moon.pos)
    kin = sum(abs(v) for v in moon.velocity)
    print(f"{pot} {kin}")
    total += pot * kin

print(f"Part 1: {total}")