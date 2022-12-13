from functools import cmp_to_key

def pair_stuff(A,B):
    A = eval(A)
    B = eval(B)
    for a,b in zip(A, B):
        if type(a) == int and type(b) == int:
            if a < b:
                return True
            elif a > b:
                return False

        elif sum([type(a)==list, type(b)==list]) == 1:
            if type(a) == int: a = [a]
            if type(b) == int: b = [b]

            res = pair_stuff(str(a),str(b))
            if res == 'equal': continue
            return res

        elif all([type(a)==list,type(b)==list]):
            if len(b) == 0 and len(a) == 0: continue
            if len(b) == 0: return False
            if len(a) == 0: return True
            
            res = pair_stuff(str(a),str(b))
            if res == 'equal': continue
            return res

    if type(A) == list and type(B) == list:
        if len(A) < len(B):
            return True
        elif len(A) > len(B):
            return False
        else:
            return 'equal'
    raise Exception('should not get here')

pairs = open('input.txt').read().split('\n\n')
part1 = 0
for i, (a,b) in enumerate(map(str.split, pairs), start=1):
    if pair_stuff(a,b):
        part1 += i
print(part1)

lines = []
for pair in map(str.split, pairs):
    lines.extend(pair)
lines.append('[[2]]')
lines.append('[[6]]')

def cmp(a,b):
    res = pair_stuff(a,b)
    if res == 'equal': return 0
    if res: return -1
    return 1

part2 = 1
for i, line in enumerate(sorted(lines, key=cmp_to_key(cmp)), start=1):
    if line in ['[[6]]', '[[2]]']:
        part2 *= i
print(part2)