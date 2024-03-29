with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

# represents a 3 wide sprite
x = 1
i = 1
p1 = []
display = ['_' for _ in range(40*6)]

for line in lines:
    cycles = 0
    match line.split():
        case ['addx', arg]:
            cycles = 2
        case ['noop']:
            cycles = 1

    for _ in range(cycles):
        if i == 20 or ((i - 20) % 40 == 0):
            p1.append(i * x)
        display[i-1] = '#' if ((i-1) % 40) in [x-1, x, x+1] else ' '
        i += 1

    match line.split():
        case ['addx', arg]:
            x += int(arg)
        case ['noop']:
            pass

print('p1', sum(p1))
print('p2:')
for i, c in enumerate(display):
    print(end=c)
    if i % 40 == 39:
        print()