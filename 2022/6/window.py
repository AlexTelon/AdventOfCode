from itertools import islice
line = open('input.txt').read()

# Inspired by the window function in kotlin.
def window(iterable, size, step=1):
    for part in zip(*[islice(iterable, i, None, step) for i in range(size)]):
        yield part

assert list(window('abcd', 2, 2)) == [('a','b'), ('c','d')]
assert list(window('abcd', 2, 1)) == [('a','b'), ('b','c'), ('c','d')]
assert list(window('abcd', 1, 1)) == [('a',),('b',),('c',),('d',)]
assert list(window('abcd', 1, 2)) == [('a',),('c',)]

def solve(size):
    for i, part in enumerate(window(line, size)):
        if len(set(part)) == size:
            return i + size - 1

print(solve(4))
print(solve(14))