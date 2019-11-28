from collections import defaultdict

directions = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0),
}

dirs = [directions[c] for line in open('input.txt') for c in line]

visited = defaultdict(int)

def move(current_pos, direction):
    global visited
    current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
    visited[current_pos] += 1
    return current_pos

santa = (0, 0)
robot = (0, 0)
move(santa, (0, 0))
move(robot, (0, 0))

for i, direction in enumerate(dirs):
    if i % 2 == 0:
        santa = move(santa, direction)
    else:
        robot = move(robot, direction)

print(len(visited))