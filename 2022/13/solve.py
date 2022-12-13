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

pairs = open('input.txt').read().split('\n\n') + ['[[6]] [[2]]']
lines = [line for pair in map(str.split,pairs) for line in pair]
print(sum(0 if larger_than(*pair) == 1 else i for i, pair in enumerate(zip(lines[::2], lines[1::2]))))

lines.sort(key=cmp_to_key(larger_than))
print((lines.index('[[6]]')+1) * (lines.index('[[2]]')+1))