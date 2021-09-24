from itertools import combinations
from math import factorial as fac

def all_combs(nums):
    tot = 0
    for r in range(1, len(nums)+1):
        tot += len(list(combinations(nums, r=r)))
        print([x for x in combinations(nums, r=r)])
    return tot
    # return sum(len([combinations(nums,r=i)]) for i in range(len(nums)))


def combinations_all_r(nums):
    tot = 0
    for r in range(1, len(nums) + 1):
        tot += fac(n) // (fac(r) * fac(n - r))
    return tot

for n in range(2, 6):
    nums = [x for x in range(n)]
    print('NEW')
    print(nums, n, " combs:", all_combs(nums))
    print(n,'math:', combinations_all_r(nums))
    # print(n, "fac: ", fac(n))