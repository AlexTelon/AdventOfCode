
directions = {
    '^': (0, 1),
    'v': (0, -1),
    '<': (-1, 0),
    '>': (1, 0),
}

dirs = [directions[c] for line in open('input.txt') for c in line]

from collections import defaultdict
visited = defaultdict(int)

current_pos = (0, 0)
visited[current_pos] += 1

for direction in dirs:
    current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
    visited[current_pos] += 1

# multiple_visits = len([key for key, value in visited if value > 1 ])

print(len(visited))