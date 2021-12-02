# Fetch and refine data.
lines = open('input.txt').read().splitlines()
instructions = []
for line in lines:
    op, num = line.split(' ')
    instructions.append((op, int(num)))


# Execute on data
hor = 0
depth = 0
aim = 0
for op, num in instructions:
    match op:
        case 'forward':
            hor += num
            depth += aim * num
        case 'up':
            aim -= num
        case 'down':
            aim += num

print(hor * depth)