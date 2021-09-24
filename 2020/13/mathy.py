import numpy as np

lines = open(0).read().splitlines()
busses = lines[1].split(',')
busses = [(int(x),i) for i,x in enumerate(busses) if x != "x"]

print(busses)
# [(7, 0), (13, 1), (59, 4), (31, 6), (19, 7)]
A = []
for outer_i, bus in enumerate(busses):
    a, b = bus
    A.append([-a if i == outer_i else 0 for i, (a,b) in enumerate(busses)])

A = np.array(A)
B = np.array([[b] for a,b in busses])
# A = np.array([[20, 10], [17, 22]])
# B = np.array([350, 500])
X = np.linalg.solve(A,B)
print(X)