from functools import cmp_to_key

def pair_stuff(A,B):
    A = eval(A)
    B = eval(B)
    for a,b in zip(A, B):
        if type(a) == int and type(b) == int:
            if a < b:
                return -1
            elif a > b:
                return 1

        elif sum([type(a)==list, type(b)==list]) == 1:
            if type(a) == int: a = [a]
            if type(b) == int: b = [b]

            res = pair_stuff(str(a),str(b))
            if res == 0: continue
            return res

        elif all([type(a)==list,type(b)==list]):
            if len(b) == 0 and len(a) == 0: continue
            if len(b) == 0: return 1
            if len(a) == 0: return -1
            
            res = pair_stuff(str(a),str(b))
            if res == 0: continue
            return res

    if type(A) == list and type(B) == list:
        if len(A) < len(B):
            return -1
        elif len(A) > len(B):
            return 1
        else:
            return 0
    raise Exception('should not get here')

pairs = open('input.txt').read().split('\n\n')
part1 = 0
for i, (a,b) in enumerate(map(str.split, pairs), start=1):
    if not pair_stuff(a,b) == 1:
        part1 += i
print(part1)

lines = ['[[2]]', '[[6]]']
for pair in map(str.split, pairs):
    lines.extend(pair)

part2 = 1
for i, line in enumerate(sorted(lines, key=cmp_to_key(pair_stuff)), start=1):
    if line in ['[[6]]', '[[2]]']:
        part2 *= i
print(part2)