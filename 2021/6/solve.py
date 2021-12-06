from collections import Counter

count = Counter(map(int, open('input.txt').read().split(',')))

#for day in range(80): #p1
for day in range(256):
    next_count = Counter()
    for t, n, in count.items():
        if t == 0:
            next_count[6] += n
        else:
            next_count[(t - 1)] += n
    next_count[8] += count[0]

    count = next_count

print(sum(count.values()))
