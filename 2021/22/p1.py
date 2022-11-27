import re
from itertools import product

# with open('sample.txt', 'r') as f:
with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

cells = set()
stuff = []
for line in lines:
    on = 'on' in line
    x_lo, x_hi, y_lo, y_hi, z_lo, z_hi = list(map(int,re.findall('-?\d+',line)))
    x = range(x_lo, x_hi+1)
    y = range(y_lo, y_hi+1)
    z = range(z_lo, z_hi+1)

    if all([set(d) <= set(range(-50,50+1)) for d in [x,y,z]]):
        if on:
            cells |= set(product(x,y,z))
        else:
            cells -= set(product(x,y,z))
print('p1', len(cells))

