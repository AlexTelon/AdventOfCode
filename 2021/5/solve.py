from collections import defaultdict

lines = open('input.txt').read().splitlines()

def debug_draw():
    # hardcoded for sample data.
    for i in range(10):
        for j in range(10):
            print(end=str(count[(j,i)]))
        print()

count = defaultdict(int)

for line in lines:
    left, right = line.split('->')
    (x, y) = list(map(int,left.split(',')))
    (xx, yy) = list(map(int,right.split(',')))

    diagonal = abs(xx - x) == abs(yy - y)
    if x == xx or y == yy or diagonal:
        if not diagonal:
            # hack to not have too deal with negative directions you need too specify a third -1 argument to range in that case.
            x, xx = sorted([x, xx])
            y, yy = sorted([y, yy])
            for i in range(x, xx+1):
                for j in range(y, yy+1):
                    count[(i, j)] += 1
        else:
            # ugly hack to get the ends to be included even if we go in negative direction.
            if x > xx:
                xx -= 1
            else:
                xx += 1

            if y > yy:
                yy -= 1
            else:
                yy += 1
            for i, j in zip(range(x, xx, -1 if x > xx else 1), range(y, yy, -1 if y > yy else 1)):
                count[(i, j)] += 1

# debug_draw()

t = 0
for k,v in count.items():
    if v > 1:
        t += 1
print(t)
