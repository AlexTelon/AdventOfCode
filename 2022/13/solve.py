from itertools import zip_longest
import math
from aocd import submit

pairs = open('input.txt').read().split('\n\n')
# pairs = open('sample.txt').read().split('\n\n')

def pair_stuff(A,B, indent=0):
    print('  '*indent+'- '+f'compare {A} vs {B}')
    indent += 1
    A = eval(A)
    B = eval(B)
    for a,b in zip(A, B):
        print('  '*indent+'- '+f'compare {a} vs {b}')
        if type(a) == int and type(b) == int:
            if a < b:
                print('  '*indent+'- '+'Left side is smaller, so inputs are in the right order')
                return True
            elif a > b:
                print('  '*indent+'- '+'Right side is smaller, so inputs are not in the right order')
                return False
        # different types. convert one to list!
        elif sum([type(a)==list,type(b)==list]) == 1:
            if type(a) == int:
                a = [a]
                print('  '*indent+'- '+f'Mixed types; convert left to {a} and retry comparison')
            if type(b) == int:
                b = [b]
                print('  '*indent+'- '+f'Mixed types; convert right to {b} and retry comparison')
            
            res = pair_stuff(str(a),str(b), indent)
            if res == 'equal':
                continue
            return res

        # if both are lists.
        elif all([type(a)==list,type(b)==list]):
            if not any(b) and not any(a):
                continue
            if not any(b):
                print('  '*indent+'- '+'Right side ran out of items, so inputs are not in the right order')
                return False
            if not any(a):
                print('  '*indent+'- '+'Left side ran out of items, so inputs are in the right order')
                return True

            res = pair_stuff(str(a),str(b), indent)
            if res == 'equal':
                continue
            return res

    if all([type(A)==list,type(B)==list]):
        # all values in a and b are equal. so check their lengths
        if len(A) < len(B):
            print('  '*indent+'- '+'Left side ran out of items, so inputs are in the right order')
            return True
        elif len(A) > len(B):
            print('  '*indent+'- '+'Right side ran out of items, so inputs are not in the right order')
            return False
        else:
            return 'equal'
    raise Exception('should not get here')
    # print('  '*indent+'- '+'Equal values, continue')
    # return 'equal'

t = 0
for i, (a,b) in enumerate(map(str.split, pairs), start=1):
    if pair_stuff(a,b):
        t += i
        print(f'right order! +{i}')
    print('....')
print(t)

# not 5879
# not 2139 (too low)
# not 2651 (too low)
# not 5684 (right answer for someone else :D )