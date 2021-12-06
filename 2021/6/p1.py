# original code for p1
current = list(map(int, open('input.txt').read().split(',')))

for day in range(80):
    new = []
    for i, fish in enumerate(current):
        if fish == 0:
            # current[i] = 6
            new.append(6)
        else:
            # current[i] = fish - 1
            new.append(fish - 1)

    current.extend([8 for fish in current if fish == 0])
    current = new

print(len(current))

