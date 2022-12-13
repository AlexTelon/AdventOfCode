from functools import cmp_to_key

def larger_than(A: str, B: str):
    A, B = eval(A), eval(B)
    for a,b in zip(A, B):
        match [a, b]:
            case [int() as a, int() as b] if a < b:  return -1
            case [int() as a, int() as b] if a > b:  return 1
            case [int() as a, int() as b] if a == b: continue
            case [list(), int() as b]:    b = [b]
            case [int() as a, list()]:    a = [a]

        res = larger_than(str(a),str(b))
        if res == 0: continue
        return res

    # Two lists that could not be distinguished by pairwise comparisons.
    if   len(A) < len(B): return -1
    elif len(A) > len(B): return 1
    else:                 return 0

pairs = open('input.txt').read().split('\n\n')
lines = ['[[2]]', '[[6]]']

part1 = 0
for i, pair in enumerate(map(str.split, pairs), start=1):
    if not larger_than(*pair) == 1:
        part1 += i
    lines.extend(pair)

lines.sort(key=cmp_to_key(larger_than))
print(part1, (lines.index('[[6]]')+1) * (lines.index('[[2]]')+1))