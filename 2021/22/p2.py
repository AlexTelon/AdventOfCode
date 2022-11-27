from dataclasses import dataclass
import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

@dataclass
class Region():
    on: bool
    x:  int
    xx: int
    y:  int
    yy: int
    z:  int
    zz: int

    def intersection(self, other):
        a =  max(self.x, other.x)
        aa = min(self.xx, other.xx)
        b =  max(self.y, other.y)
        bb = min(self.yy, other.yy)
        c =  max(self.z, other.z)
        cc = min(self.zz, other.zz)
        if a > aa or b > bb or c > cc:
            return None
        # new  old
        # self other
        # ---------
        #  on   on | # Other added what in the intersection already. remove it so we dont overcount.
        # off   on | # Other added what in the intersection already. remove it since self is 'off'
        # off  off | # Other removed what in the intersection already. Add it so we dont remove twice.
        #  on  off | # Other removed what in the intersection already. Add it since self is 'on'
        # In summary. Reverse the effect of other in the intersection area.
        return Region(not other.on, a,aa,b,bb,c,cc)

    def volume(self):
        dx = self.xx-self.x
        dy = self.yy-self.y
        dz = self.zz-self.z
        sign = [-1,1][self.on]
        return sign * (dx+1) * (dy+1) * (dz+1)


regions = []
for line in lines:
    regions.append(Region('on' in line, *map(int,re.findall('-?\d+',line))))

# The area for p2 is too large to consider each cell individually.
# Instead we keep track of regions and use volume calculations.
# Where these regions overlap we need to ensure that we are not overcounting.


# The idea is, add a region (if its on) and for all intersections with previous regions
# consider if it overlaps with any of them and if we do add this region to the list of previous regions.
# Each region has a volume. The volume can either be added or removed from the total.
# See table below for what to do when:
# new  prev
# ---------
#  on   on | # Other added what in the intersection already.   Remove intersection volume so we dont overcount.
# off   on | # Other added what in the intersection already.   Remove intersection volume since self is 'off'
# off  off | # Other removed what in the intersection already. Add intersection volume so we dont remove twice.
#  on  off | # Other removed what in the intersection already. Add intersection volume since self is 'on'
previous = []
for region in regions:
    # Find all intersections between this cube an all previous.
    intersections = []
    for prev in previous:
        x = region.intersection(prev)
        if x:
            intersections.append(x)

    if region.on:
        previous.append(region)
    previous.extend(intersections)

print('p2', sum(region.volume() for region in previous))
