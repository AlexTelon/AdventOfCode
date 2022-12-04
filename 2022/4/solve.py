with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def parse(a):
    lo, hi = map(int,a.split('-'))
    return set(range(lo,hi+1))

p1 = 0
p2 = 0
for line in lines:
    a, b = line.split(',')
    lo = parse(a)
    hi = parse(b)
    p2 += any(lo.intersection(hi))
    p1 += (lo <= hi or hi <= lo)

# p1
print(p1)
# p2
print(p2)