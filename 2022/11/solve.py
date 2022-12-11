from dataclasses import dataclass
import re
from typing import Callable, List
from aocd import submit

# groups = open('sample.txt').read().split('\n\n')
groups = open('input.txt').read().split('\n\n')

@dataclass
class Monkey():
    items: List[int]
    operation: str
    should_throw: Callable
    if_true: int
    if_false: int


t = 0
monkeys: List[Monkey] = []
for y, group in enumerate(groups):
    for line in group.splitlines():
        if 'items' in line:
            items = list(map(int,re.findall(r'-?\d+', line)))
        elif 'Operation' in line:
            _, exp = line.split('=')
            operation = f'old = {exp}'
        elif 'Test' in line:
            num = list(map(int,re.findall(r'-?\d+', line)))[0]
            print('test', num)
            should_throw = lambda x: x % num == 0
        elif 'If true' in line:
            if_true = list(map(int,re.findall(r'-?\d+', line)))[0]
        elif 'If false' in line:
            if_false = list(map(int,re.findall(r'-?\d+', line)))[0]

    monkey = Monkey(items, operation, should_throw, if_true, if_false)
    monkey.inspected = 0
    monkey.num = num
    monkeys.append(monkey)
for r in range(20):
    print('round', r)

    for monkey in monkeys:
        new = []
        for item in monkey.items:
            monkey.inspected += 1
            old = item
            exec(monkey.operation, globals())
            old //= 3
            new.append(old)
        monkey.items = new

        # tests
        removed = []
        for item in monkey.items:
            # if monkey.should_throw(item):
            if item % monkey.num == 0:
                i = monkey.if_true
            else:
                i = monkey.if_false
            
            removed.append(item)
            monkeys[i].items.append(item)

        for x in removed:
            monkey.items.remove(x)

for m in sorted(monkeys, key= lambda m: m.inspected):
    print(m.inspected)

print('p1', 332*334)
# not 124593    (357*349)