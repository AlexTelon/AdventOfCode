crabs = list(map(int,open('input.txt').read().split(',')))
# p1
# def dist(a, b):
#     return abs(a-b)

def dist(a, b):
    n = abs(a-b)
    return n*(n+1)//2

# My original solution did not check all potential positions.
# Only positions that one crab was occupying already. This fixes that.
candidates = range(min(crabs), max(crabs))
print(min(sum(dist(pos, crab) for crab in crabs) for pos in candidates))