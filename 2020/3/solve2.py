from aocd import data, submit, get_data

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

grid = []
for line in lines:
    grid.append(line)

def solve(dx,dy):
    x, y = 0, 0
    t = 0
    try:
        while True:
            c = grid[y][x]
            t += c == '#'
            x = (x + dx) % len(grid[0])
            y += dy
    except Exception as e:
        ...
    return t
# p1
print('p1', solve(dx = 3, dy = 1))

# p2
t = 1

t *= solve(dx = 1, dy = 1)
t *= solve(dx = 3, dy = 1)
t *= solve(dx = 5, dy = 1)
t *= solve(dx = 7, dy = 1)
t *= solve(dx = 1, dy = 2)
print('p2', t)