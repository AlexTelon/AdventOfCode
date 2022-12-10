from aocd import submit

with open('input.txt', 'r') as f:
# with open('sample.txt', 'r') as f:
    lines = f.read().splitlines()

# lines = """noop
# addx 3
# addx -5""".splitlines()

x = 1
i = 1
p1 = []
for line in lines:
    cycles = 0
    match line.split():
        case ['addx', arg]:
            cycles = 2
        case ['noop']:
            cycles = 1
            pass
        case _:
            raise Exception('missing')

    # print(i)
    for _ in range(cycles):
        if i == 20 or ((i - 20) % 40 == 0):
            print(i, x, i * x)
            p1.append(i * x)
        i += 1

    match line.split():
        case ['addx', arg]:
            x += int(arg)
        case ['noop']:
            pass
        case _:
            raise Exception('missing')

print('end', p1, sum(p1))
submit(sum(p1))

# not 14000