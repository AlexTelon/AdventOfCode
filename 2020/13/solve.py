import math

lines = open(0).read().splitlines()
for line in lines:
    print(line)

goal = int(lines[0])
busses = list(map(int,lines[1].replace('x,', "").split(',')))

print(goal, busses)

stuff = [goal // buss for buss in busses]

lowest = math.inf
buss_id = -1

for buss in busses:
    tmp = 0
    while tmp < goal:
        tmp += buss

    if tmp < lowest:
        lowest = min(lowest, tmp)
        buss_id = buss

wait = lowest - goal
print(wait)
print(buss_id)
print(buss_id * wait)