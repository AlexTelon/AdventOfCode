groups = open(0).read().split("\n\n")
total_1, total_2 = 0, 0

for group in groups:
    total_1 += len(set.union(*[set(line) for line in group.splitlines()]))
    total_2 += len(set.intersection(*[set(line) for line in group.splitlines()]))

print(total_1)
print(total_2)

exit()
# Add dummy newline at end.
lines.append("")

current = []
total_2 = 0
for line in lines:
    if line == "":
        # first way
        common = current[0]
        for person in current[1:]:
            common = common.intersection(person)
        # Same thing but short and not error-prone
        # common = set.intersection(*current)

        print(f"+{len(common)}")
        total_2 += len(common)

        # Start of new group.
        current = []
        continue

    # During competition.
    new = set()
    print(line)
    for c in line:
        new.add(c)
    current.append(new)

    # Same thing but shorter and simpler to get right
    # current.append(set(line))

print(total_2)