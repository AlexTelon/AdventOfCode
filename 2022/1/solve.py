with open('input.txt', 'r') as f:
    groups = f.read().split('\n\n')

# p1
print(max(sum(int(line) for line in g.splitlines()) for g in groups))
# p2
print(sum(sorted([sum(int(line) for line in g.splitlines()) for g in groups])[-3:]))