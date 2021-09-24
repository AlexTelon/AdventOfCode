import networkx as nx

lines = open('tmp.txt').read().splitlines()

g = nx.Graph([item.split(')') for item in lines])

part_1 = sum(nx.shortest_path_length(g, source='COM').values())

# -2 because its not from SAN to YOU, but from the "parents" of both to eachother.
# So take away initial step from both getting to their "parents".
part_2 = nx.shortest_path_length(g, source='SAN', target='YOU') - 2
print(part_1, part_2)

print()
print()

lines = open('input.txt').read().splitlines()
lines = [tuple(line.split()) for line in lines]
print(lines)
g = nx.Graph(lines)
print(g.edges())
print(g.nodes())
print(nx.shortest_path_length(g, '1', '3'))
print(nx.shortest_path(g, '1', '3'))
print("end")
# for line in lines:
#     print(line)
