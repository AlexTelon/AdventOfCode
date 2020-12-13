import math
lines = open(0).read().splitlines()
busses = lines[1].split(',')
busses = [(int(x),i) for i,x in enumerate(busses) if x != "x"]

print(busses)

values = [a for a,b in busses]
diffs =  [b for a,b in busses]
# print(values)

def is_exit_condition(values):
    vals = set([x - diffs[i] for i,x in enumerate(values)])
    return len(vals) == 1
from collections import defaultdict

steps = 0
mult_counter = defaultdict(int)
while True:
    tmp = sorted(values)
    min1 = tmp[0]
    max2 = tmp[-1]

    i1 = values.index(min1)
    i2 = values.index(max2)

    diff1 = diffs[i1]
    diff2 = diffs[i2]
    delta = diff2 - diff1
    
    goal = max2 - delta
    left_to_goal = goal - min1

    step = busses[i1][0]

    mult = max(1, math.ceil(left_to_goal / step))
    # mult_counter[mult] += 1
    values[i1] += step * mult

    print(values)
    print(f"{min1} needs to increase to {goal} or more, left: {left_to_goal}, steps: {mult}")

    # values[i] += busses[i][0]

    steps += 1
    if is_exit_condition(values):
        print("done")
        print(values)
        print(steps)
        print(f'time is {min(values)}')
        break
    if steps > 5:
        print(f'stop iterations!, time is {min(values)}')
        break

# print('mult counter')
# for k,v in mult_counter.items():
#     print(k,v)


print(f'time is {min(values)}')