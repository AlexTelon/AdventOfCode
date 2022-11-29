from itertools import product
from aocd import get_data, submit

lines = get_data(year=2020, day=1).splitlines()
nums = [int(x) for x in lines]

seen = set()
for x in nums:
    if 2020-x in seen:
        print('p1',(2020-x) * x)
        break
    seen.add(x)

seen = set()
for x,y in product(nums, repeat=2):
    if 2020-x-y in seen:
        print('p2', (2020-x-y) * x * y)
        break
    seen.add(x)
