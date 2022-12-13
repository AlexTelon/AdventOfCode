from functools import cmp_to_key

def larger_than(A: str, B: str):
    A, B = eval(A), eval(B)
    for a,b in zip(A, B):
        match a, b:
            case [int(), int()]:
                if   a < b: return -1
                elif a > b: return 1
                else: continue
            case [list(), int() as b]:
                b = [b]
            case [int() as a, list()]:
                a = [a]

        res = larger_than(str(a),str(b))
        if res == 0: continue
        return res

    if (type(A) == list) and (type(B) == list):
        if   len(A) < len(B): return -1
        elif len(A) > len(B): return 1
        else:                 return 0
    raise Exception('should not get here')

pairs = open('input.txt').read().split('\n\n')
lines = ['[[2]]', '[[6]]']

part1, part2 = 0, 1
for i, pair in enumerate(map(str.split, pairs), start=1):
    if not larger_than(*pair) == 1:
        part1 += i
    lines.extend(pair)

for i, line in enumerate(sorted(lines, key=cmp_to_key(larger_than)), start=1):
    if line in ['[[6]]', '[[2]]']:
        part2 *= i

print(part1, part2)