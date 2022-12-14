def lt(A, B):
    for a,b in zip(A, B):
        match [a, b]:
            case [int() as a, int() as b] if a < b:  return 1
            case [int() as a, int() as b] if a > b:  return -1
            case [int() as a, int() as b] if a == b: continue
            case [list(), int() as b]:       b = [b]
            case [int() as a, list()]:       a = [a]
        res = lt(a,b)
        if res == 0: continue
        return res

    # Two lists that could not be distinguished by pairwise comparisons.
    if   len(A) < len(B): return 1
    elif len(A) > len(B): return -1
    else:                 return 0

part1, _2, _6 = 0, 1, 2
for i, pair in enumerate(map(str.split, open('input.txt').read().split('\n\n'))):
    l, r = map(eval, pair)
    if lt(l,r) == 1: part1 += i+1
    _2 += sum(lt(x,[[2]]) == 1 for x in (l,r))
    _6 += sum(lt(x,[[6]]) == 1 for x in (l,r))

print(part1, _2*_6)