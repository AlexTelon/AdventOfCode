import re

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

# Reverse after for correct order
data = [
    [],
    ['L','C','G','M','Q'],
    ['G','H','F','T','C','L','D','R'],
    ['R','W','T','M','N','F','J','V'],
    ['P','Q','V','D','F','J'],
    ['T', 'B', 'L', 'S', 'M', 'F', 'N'],
    ['P','D','C','H','V','N','R'],
    ['T','C','H'],
    ['P','H','N','Z','V','J','S','G'],
    ['G','H','F','Z'],
]
data = [x[::-1]for x in data]


for line in lines:
    i, start, dest  = map(int,re.findall(r'-?\d+', line))
    # p1
    # for _ in range(i):
    #     item = data[start].pop()
    #     data[dest].append(stuff[::-1])

    # p2
    stuff = []
    for _ in range(i):
        item = data[start].pop()
        stuff.append(item)
    data[dest].extend(stuff[::-1])

for x in data:
    if x:
        print(end=x[-1])