from dataclasses import dataclass
import math
import re
from typing import List

groups = open('input.txt').read().split('\n\n')

@dataclass
class Monkey():
    items: List[int]
    operation: str
    div: int
    if_true: int
    if_false: int


monkeys: List[Monkey] = []
for y, group in enumerate(groups):
    for line in group.splitlines():
        if 'items' in line:
            items = list(map(int,re.findall(r'-?\d+', line)))
        elif 'Operation' in line:
            _, exp = line.split('=')
            operation = f'old = {exp}'
        elif 'Test' in line:
            div = list(map(int,re.findall(r'-?\d+', line)))[0]
        elif 'If true' in line:
            if_true = list(map(int,re.findall(r'-?\d+', line)))[0]
        elif 'If false' in line:
            if_false = list(map(int,re.findall(r'-?\d+', line)))[0]

    monkey = Monkey(items, operation, div, if_true, if_false)
    monkey.inspected = 0
    
    monkeys.append(monkey)

# to keep the numbers getting too large!
# least common multiple is safe to do modulu with.
mod = math.lcm(*[m.div for m in monkeys])

for r in range(10000):
    # Monkey inspections.
    for monkey in monkeys:
        new = []
        for item in monkey.items:
            monkey.inspected += 1
            old = item
            exec(monkey.operation, globals())
            # p1 logic
            # old //= 3
            # p2 logic
            old %= mod
            new.append(old)
        monkey.items = new

        # Monkey tests.
        for item in monkey.items:
            if item % monkey.div == 0:
                i = monkey.if_true
            else:
                i = monkey.if_false
            monkeys[i].items.append(item)

        # Monkey never throws to itself in my input. So all are removed.
        monkey.items = []

# print('p1', 332*334)
# print('p2', 159957*159983)
print(math.prod([m.inspected for m in sorted(monkeys, key=lambda m: m.inspected)[-2:]]))