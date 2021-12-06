from collections import Counter

count = Counter(map(int, open('input.txt').read().split(',')))

for _ in range(256): # p1 use 80
    count = Counter({k-1:v for k,v in count.items()})
    count[8] += count[-1]
    count[6] += count[-1]
    del count[-1]

print(sum(count.values()))
