lines = open('input.txt').read().splitlines()

def rotate(direction, vector):
    """Takes a direction N or L and rotates a vector accordingly around origo"""
    # Swap and Negate
    # Draw the point (2, 1) on a coodrinate axis and rotate 4 times.
    # Note how x,y is always swaped. And depending on if you rotate left or right you negate one of the numbers.
    if direction == 'L':
        vector[0], vector[1] = vector[1], -vector[0]
    else:
        vector[0], vector[1] = -vector[1], vector[0]
    return vector

directions = {
    'N': (1, 0),
    'E': (0, 1),
    'S': (-1, 0),
    'W': (0, -1),
}

dirs = "NESW"
dir = 'E'
pos = [0, 0]
forward_vector = [1, 10]

for line in lines:
    c = line[0]
    num = int(line[1:])

    if c in 'NESW':
        vector = directions[c]
        forward_vector[0] += vector[0] * num
        forward_vector[1] += vector[1] * num
        # print(f"new forward_vector {forward_vector}")

    if c in 'LR':
        assert num in [0, 90, 180, 270]
        num = [0, 90, 180, 270].index(num)

        for i in range(num):
            rotate(c, forward_vector)
        # print(f"new forward_vector {forward_vector} rotated {c} {num} times")

    if c == 'F':
        # print(f"forward_vector: {forward_vector} {num} times")
        pos[0] += forward_vector[0] * num
        pos[1] += forward_vector[1] * num
    # print(pos)

print(f'final pos {pos}')
print(sum(abs(p) for p in pos))