vowels = 'aeiou'
# one twice in a row
not_allowed = ['ab', 'cd', 'pq', 'xy']

p1 = 0
for line in open('input.txt').read().splitlines():
    if any(word in line for word in not_allowed):
        continue

    if sum(c in vowels for c in line) >= 3:

        if not any(a == b for a,b in zip(line, line[1:])):
            continue

        p1 += 1


print(p1)
# part 1: 05:33 

p2 = 0
for line in open('input.txt').read().splitlines():

    # Find xyx like patterns or aaa is also allowed.
    if not any(a == c for a,b,c in zip(line, line[1:], line[2:])):
        continue

    for i, (a,b) in enumerate(zip(line, line[1:])):
        if a+b in line[i+2:]:
            p2 += 1
            break

print(p2)