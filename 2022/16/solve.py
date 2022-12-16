from collections import defaultdict
from copy import copy
import re

# lines =  open('in.txt').read().splitlines()
lines =  open('sample.txt').read().splitlines()

rooms = defaultdict(list)
rooms_rate = {}

for line in lines:
    # Valve TN has flow rate=0; tunnels lead to valves IX, ZZ
    rate = int(re.findall(r'-?\d+', line)[0])
    _, name, *_ = line.split()
    name = name.strip()
    _, r = line.split('valves ')
    leads_to = r.split(',')
    print(name, rate, leads_to)
    leads_to = [x.strip() for x in leads_to if x.strip() != '']


    rooms[name].extend(leads_to)
    rooms_rate[name] = rate

for name, leads_to in rooms.items():
    print(name, leads_to, rooms_rate[name])


flow_rate = 0
t = 0
room = 'AA'

def bfs(current, time_left, alread_used:set):
    # time_diff, added_flow and which one we choose?
    # or just return the goal?
    t = 0
    seen = set()
    stack = [current]

    options = {}

    while stack:
        node = stack.pop(0) # dfs: pop() bfs: pop()
        t += 1 # moving takes time
        if node not in seen:
            if node not in alread_used:
                rate = rooms_rate[node]
                options[node] = (rate * (time_left - t - 1))
                print(f'node, {node}, {rate=}, {t}')

            seen.add(node)

            # Next visit all connected nodes
            for n in rooms[node]:
                stack.append(n)
            print('')
    
    return max((flow, item, t) for item, flow in options.items())

def max_flow(current, flow=0, time_left=30, open_valves: set=None, visited:set=None):
    visited.add(current)

    # walk through this room is always 1 min.
    time_left -= 1
    options = []
    print(f'{current=} {time_left=}')
    f = rooms_rate[current]
    # cannot or should not spend time opening this valve
    if f > 0 and current not in open_valves:
        # If we open valve in this room. Takes another minute.
        time_left -= 1
        a = flow + f * (time_left)
        print(f'open valve in {current}:  {flow} + {f} * {time_left} = {a} ')
        open_valves.add(current)
        options = [a]


    for adj in rooms[current]:
        if adj not in visited:
            # print(f'walk to {adj} {visited=}')
            options.append(flow + max_flow(adj, flow, time_left=time_left, open_valves=copy(open_valves), visited=copy(visited)))

    return max(options)

print()
print(max_flow('AA', flow=0, time_left=31, open_valves=set(), visited=set()))
# time_left = 30
# opened = set()
# flow, room, t= bfs('AA', time_left, opened)
# print(flow, room)
# time_left -= t
# opened.add(room)

# flow, room, t= bfs(room, time_left, opened)
# print(flow, room)


# # not 504