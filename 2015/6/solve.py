from collections import defaultdict

lines = open('input.txt').read().splitlines()

# Grid where everything is off (0) by default.
grid = defaultdict(int)

def action(a,b, func):
    global grid
    x_range = range(a[0], b[0]+1)
    y_range = range(a[1], b[1]+1)
    for x in x_range:
        for y in y_range:
            grid[(x,y)] = func(grid[(x,y)])

data = []

actions = {
    'turn_on':  lambda x: x+1,
    'turn_off': lambda x: max(0, x-1),
    'toggle': lambda x: x+2,
}

for i, line in enumerate(lines):
    op, a, _, b = line.split()
    a = tuple(int(x) for x in a.split(','))
    b = tuple(int(x) for x in b.split(','))
    print(i, len(lines))
    action(a, b, actions[op])

print(sum(grid.values()))