import itertools

raw = 'abcde'
n = len(raw)
data = [c for c in raw]
perms = itertools.permutations(data, n)

dictionary = {}

for p in perms:
    p = tuple(sorted(p))
    dictionary[p] = 'a'

print(dictionary)