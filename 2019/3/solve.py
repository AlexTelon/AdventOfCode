from collections import defaultdict


lines = [line.split(',') for line in open('input.txt')]

directions = {
    'R' : (0, 1),
    'L' : (0, -1),
    'U' : (1, 0),
    'D' : (-1, 0),
}

visited = defaultdict(set)
visited_count = defaultdict(dict)

pos = defaultdict(tuple)
pos[0] = (0,0)
pos[1] = (0,0)

for i, line in enumerate(lines):
    count = 0
    for order in line:
        letter = order[0]
        num = int(order[1:])

        direction = directions[letter]

        for step in range(num):
            count += 1
            pos[i] = (pos[i][0] + direction[0], pos[i][1] + direction[1])
            visited[i].add(pos[i])
            visited_count[i][pos[i]] = count


intersections = visited[0].intersection(visited[1])

print("part1: ", min(abs(x[0]) + abs(x[1]) for x in intersections))
print("part2: ", min(visited_count[0][x] + visited_count[1][x] for x in intersections))