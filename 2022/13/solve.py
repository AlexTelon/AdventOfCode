from aocd import submit
from functools import cmp_to_key


def pair_stuff(A,B, indent=0):
    # print('  '*indent+'- '+f'compare {A} vs {B}')
    indent += 1
    A = eval(A)
    B = eval(B)
    for a,b in zip(A, B):
        # print('  '*indent+'- '+f'compare {a} vs {b}')
        if type(a) == int and type(b) == int:
            if a < b:
                # print('  '*indent+'- '+'Left side is smaller, so inputs are in the right order')
                return True
            elif a > b:
                # print('  '*indent+'- '+'Right side is smaller, so inputs are not in the right order')
                return False
        # different types. convert one to list!
        elif sum([type(a)==list,type(b)==list]) == 1:
            if type(a) == int:
                a = [a]
                # print('  '*indent+'- '+f'Mixed types; convert left to {a} and retry comparison')
            if type(b) == int:
                b = [b]
                # print('  '*indent+'- '+f'Mixed types; convert right to {b} and retry comparison')
            
            res = pair_stuff(str(a),str(b), indent)
            if res == 'equal':
                continue
            return res

        # if both are lists.
        elif all([type(a)==list,type(b)==list]):
            # if not any(b) and not any(a):
            if len(b) == 0 and len(a) == 0:
                continue
            if len(b) == 0:
                # print('  '*indent+'- '+'Right side ran out of items, so inputs are not in the right order')
                return False
            if len(a) == 0:
                # print('  '*indent+'- '+'Left side ran out of items, so inputs are in the right order')
                return True

            res = pair_stuff(str(a),str(b), indent)
            if res == 'equal':
                continue
            return res

    if all([type(A)==list,type(B)==list]):
        # all values in a and b are equal. so check their lengths
        if len(A) < len(B):
            # print('  '*indent+'- '+'Left side ran out of items, so inputs are in the right order')
            return True
        elif len(A) > len(B):
            # print('  '*indent+'- '+'Right side ran out of items, so inputs are not in the right order')
            return False
        else:
            return 'equal'
    raise Exception('should not get here')
    # # print('  '*indent+'- '+'Equal values, continue')
    # return 'equal'

# pair_stuff('[[[]]]','[[]]')
# exit()
if False:
    pairs = open('input.txt').read().split('\n\n')
    # pairs = open('sample.txt').read().split('\n\n')

    t = 0
    for i, (a,b) in enumerate(map(str.split, pairs), start=1):
        if pair_stuff(a,b):
            t += i
            print(f'right order! +{i}')
        print('....')
    print(t)
# exit()


# pairs = open('sample.txt').read().split('\n\n')
pairs = open('input.txt').read().split('\n\n')
lines = []
for a,b in map(str.split, pairs):
    lines.append(a)
    lines.append(b)
lines.append('[[2]]')
lines.append('[[6]]')

# bubble sort?
def cmp(a,b):
    res = pair_stuff(a,b)
    if res == 'equal':
        return 0
    if res:
        return -1
    return 1
    # return not res
# lambda cmp a,b =  if pair_stuff == 

for line in lines:
    print(line)
print()
print()
p2 = 1
for i, line in enumerate(sorted(lines, key = cmp_to_key(cmp))):
    print(i, line)
    if line in ['[[6]]', '[[2]]']:
        p2 *= (i+1)

# print(lines.index('[[6]]'))
# print(lines.index('[[2]]'))


print(p2)