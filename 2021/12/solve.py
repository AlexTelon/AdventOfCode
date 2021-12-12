from collections import defaultdict, deque

lines = open('input.txt').read().splitlines()

graph = defaultdict(list)
for line in lines:
    a,b = line.split('-')
    graph[a].append(b)
    graph[b].append(a)


visited = deque()
paths = set()

def seen(cave:str):
    if cave.isupper():
        # always allow revisiting a large cave!
        return False
    if cave in ['start', 'end']:
        # Never allow revisiting start/end cave!
        return cave in visited
    
    # p2
    # In p2 we allow for any 1 small cave to be revisited once.
    small_caves = [cave for cave in visited if cave.islower()]
    if len(small_caves) - len(set(small_caves)) == 0:
        # No duplicates small caves, will allow a potential duplicate!
        return False
    else:
        return cave in visited


def dfs(graph, node):
    global visited
    visited.append(node)

    for adj in graph[node]:
        if not seen(adj):
            if adj == 'end':
                # print(">", ','.join(visited) + ',' +adj)
                paths.add(tuple(visited) + (adj,))
            else:
                dfs(graph, adj)
    if visited:
        visited.pop()


dfs(graph, 'start')
print(len(paths))