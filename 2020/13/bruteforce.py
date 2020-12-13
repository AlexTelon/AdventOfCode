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

steps = 0
while True:
    # print(values)
    i = values.index(min(values))
    values[i] += busses[i][0]
    steps += 1

    if is_exit_condition(values):
        print("done")
        print(values)
        print(steps)
        print(f'time is {min(values)}')
        break
    # if steps > 2000:
    #     print(f'stop iterations!, time is {min(values)}')
    #     break
