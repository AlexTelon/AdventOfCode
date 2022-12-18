from itertools import combinations

lines = open('in.txt').read().splitlines()
# lines = open('sample.txt').read().splitlines()
# lines = """1,1,1
# 1,1,2
# 1,1,4
# 1,1,5
# """.splitlines()

# Connected groups.
groups = []

positions = set()
for line in lines:
    x,y,z = map(int,line.split(','))
    positions.add((x,y,z))

def adjecent(a, b):
    diffs = []
    for x, xx in zip(a,b):
        diffs.append(abs(xx-x))
    res = sorted(diffs) == [0,0,1]
    return res

t = len(positions) * 6

connected = 0
for pos, other in combinations(positions, r=2):
    if pos == other: continue
    connected += adjecent(pos, other)

print(t- connected*2)