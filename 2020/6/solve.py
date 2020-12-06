lines = open('input.txt').read().splitlines()
# Add dummy newline at end.
lines.append("")


current = []
total_1 = 0
total_2 = 0
for line in lines:
    if line == "":
        # first way
        # common = current[0]
        # for person in current[1:]:
        #     common = common.intersection(person)

        total_1 += len(set.union(*current))

        common = set.intersection(*current)
        #print(f"+{len(common)}")
        total_2 += len(common)

        # Start of new group.
        current = []
        continue

    # During competition.
    # new = set()
    # for c in line:
    #     new.add(c)
    # current.append(new)

    #Cleaned up version.
    current.append(set(line))


print(total_1)
print(total_2)