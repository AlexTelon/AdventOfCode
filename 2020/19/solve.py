from collections import defaultdict
from itertools import chain

input_file = 'input.txt'
# input_file = 'sample.txt'

lines = open(input_file).read().splitlines()

if input_file == 'input.txt':
    rules = {
        53: [(21, 35), (84, 72)],
        129: [(72, 68), (35, 97)],
        29: [(110, 35), (45, 72)],
        12: [(26, 72), (2, 35)],
        101: [(72, 103), (35, 52)],
        5: [(40, 35), (49, 72)],
        94: [(35, 57), (72, 58)],
        87: [(86, 72), (69, 35)],
        1: [(63, 35), (61, 72)],
        119: [(96, 35)],
        59: [(35, 96), (72, 118)],
        14: [(96, 35), (74, 72)],
        20: [(78, 72), (26, 35)],
        120: [(72, 35), (72, 72)],
        82: [(51, 72), (93, 35)],
        104: [(35, 36), (72, 106)],
        96: [(35, 72), (72, 72)],
        25: [(89, 35)],
        130: [(56, 35), (14, 72)],
        57: [(35, 112), (72, 21)],
        24: [(38, 35), (95, 72)],
        126: [(72, 35), (35, 35)],
        39: [(35, 41), (72, 46)],
        113: [(127, 35), (22, 72)],
        114: [(72, 87), (35, 129)],
        3: [(72, 107), (35, 132)],
        64: [(72, 98), (35, 9)],
        124: [(80, 35), (126, 72)],
        117: [(35, 80), (72, 120)],
        122: [(72, 1), (35, 43)],
        11: [(42, 31)],
        76: [(58, 72), (71, 35)],
        52: [(99, 96)],
        84: [(35, 35)],
        88: [(35, 37), (72, 106)],
        67: [(118, 72), (80, 35)],
        43: [(19, 72), (91, 35)],
        4: [(113, 72), (23, 35)],
        85: [(72, 80), (35, 15)],
        36: [(112, 35), (118, 72)],
        32: [(72, 112), (35, 79)],
        62: [(35, 77), (72, 81)],
        23: [(25, 35), (6, 72)],
        116: [(96, 35), (112, 72)],
        8: [(42,)],
        105: [(131, 35), (15, 72)],
        27: [(84, 72), (15, 35)],
        133: [(72, 104), (35, 76)],
        16: [(72, 72)],
        22: [(72, 112), (35, 80)],
        37: [(15, 35)],
        41: [(120, 35), (112, 72)],
        91: [(72, 82), (35, 88)],
        109: [(35, 100), (72, 34)],
        15: [(35, 72), (35, 35)],
        92: [(35, 18), (72, 50)],
        110: [(35, 4), (72, 114)],
        123: [(35, 112), (72, 120)],
        46: [(72, 16), (35, 120)],
        26: [(120, 72), (96, 35)],
        83: [(123, 72), (33, 35)],
        111: [(90, 35), (94, 72)],
        10: [(72, 101), (35, 130)],
        45: [(133, 72), (111, 35)],
        77: [(10, 72), (125, 35)],
        90: [(35, 44), (72, 105)],
        99: [(72,), (35,)],
        93: [(112, 35), (112, 72)],
        13: [(32, 35), (124, 72)],
        56: [(72, 96), (35, 15)],
        61: [(72, 73), (35, 28)],
        6: [(99, 74)],
        58: [(72, 120), (35, 16)],
        95: [(72, 80), (35, 96)],
        60: [(99, 21)],
        63: [(72, 20), (35, 83)],
        42: [(72, 122), (35, 29)],
        38: [(120, 72), (16, 35)],
        51: [(131, 35), (16, 72)],
        17: [(35, 84), (72, 84)],
        131: [(99, 99)],
        100: [(115, 35), (117, 72)],
        55: [(35, 2), (72, 116)],
        21: [(99, 72), (35, 35)],
        89: [(72, 72), (35, 35)],
        34: [(22, 72), (85, 35)],
        18: [(96, 35), (131, 72)],
        75: [(5, 72), (108, 35)],
        108: [(3, 72), (102, 35)],
        49: [(72, 117), (35, 127)],
        102: [(35, 132), (72, 41)],
        0: [(8, 11)],
        79: [(72, 35)],
        19: [(72, 12), (35, 92)],
        71: [(21, 35)],
        98: [(35, 15), (72, 131)],
        81: [(35, 109), (72, 70)],
        106: [(72, 131), (35, 16)],
        30: [(67, 35), (115, 72)],
        50: [(15, 99)],
        86: [(35, 112)],
        69: [(72, 21), (35, 89)],
        2: [(35, 21), (72, 80)],
        73: [(35, 60), (72, 59)],
        33: [(72, 15), (35, 118)],
        70: [(72, 121), (35, 30)],
        31: [(35, 62), (72, 54)],
        65: [(24, 72), (55, 35)],
        127: [(35, 15), (72, 74)],
        118: [(35, 35), (72, 99)],
        78: [(15, 72), (96, 35)],
        68: [(72, 89), (35, 120)],
        112: [(35, 72)],
        7: [(65, 35), (48, 72)],
        44: [(74, 72), (80, 35)],
        115: [(35, 128), (72, 74)],
        74: [(35, 72), (99, 35)],
        125: [(35, 64), (72, 47)],
        40: [(98, 35), (17, 72)],
        121: [(72, 53), (35, 119)],
        103: [(72, 15), (35, 126)],
        9: [(35, 16), (72, 84)],
        97: [(84, 35), (16, 72)],
        80: [(35, 72), (72, 35)],
        47: [(35, 66), (72, 106)],
        28: [(50, 35), (27, 72)],
        107: [(80, 72), (126, 35)],
        128: [(72, 35), (99, 72)],
        132: [(35, 80), (72, 118)],
        54: [(75, 35), (7, 72)],
        66: [(72, 84), (35, 89)],
        48: [(39, 35), (13, 72)],
        35: ["a"],
        72: ["b"],
    }
else:
    rules = {
        0: [(4, 1, 5)],
        1: [(2, 3), (3, 2)],
        2: [(4, 4), (5, 5)],
        3: [(4, 5), (5, 4)],
        4: "a",
        5: "b",
    }

seen = set()

def replace(values, match, new):
    tmp = []
    for i, x in enumerate(values):
        if x == match:
            tmp.append(new)
        elif isinstance(x, tuple):
            x = replace(x, match, new)
            tmp.append(x)
        else:
            tmp.append(x)
    return tuple(tmp)

    
# values = (0, 1, 2)
# a = replace(values, 2, 'a')
# print(a)
# assert(a == (0, 1, 'a'))
# assert(values == (0, 1, 2))
# exit()

# values = [0, 1, 2]
# replace(values, 2, 'a')
# assert(values == [0, 1, 'a'])

# values = [[0, 2], 1, 2]
# replace(values, 2, 'a')
# assert(values == [[0, 'a'], 1, 'a'])

# values = [[2, [0, 2]], 1, 2]
# a = replace_new(values, 2, 'a')
# replace(values, 2, 'a')
# assert(values == [['a', [0, 'a']], 1, 'a'])
# assert(a == values)

# values = [['aa', 3], ['bb', 3]]
# a = replace(values, 3, 'ab')
# assert(a == [['aa', 'ab'], ['bb', 'ab']])

# exit()

def is_resolved(values):
    if isinstance(values, int):
        return False
    if isinstance(values, str):
        return all(c in ['a', 'b'] for c in values)
    return all(is_resolved(x) for x in values)

assert(is_resolved([('b', 'a')]))
assert(is_resolved([('b', 'a'), ('ba', 'b')])) # -> ['ba', 'bab']
assert(is_resolved([[['aa', 'ab'], ['bb', 'ab']], [['ab', 'aa'], ['ab', 'bb']]]))
# exit()

# def bake(values):
#     things = []
#     for sub in values:
#         stuff = []
#         for x in sub:
#             stuff += x
#         # things.append("".join([x for x in sub]))
#         things.append("".join(stuff))
#     return things

# def bake_old(values):
#     if all(isinstance(x, str) for x in values):
#         return "".join(values)
#     things = []
#     for sub in values:
#         stuff = []
#         if isinstance(sub, tuple) or isinstance(sub, list):
#             # things.append("".join(bake(sub)))
#             things.append(bake(sub))
#         else:
#             things.append(sub)
#     return tuple(things)

def bake_inner(values):
    #('a',) -> 'a'
    #('a','b') -> 'ab'
    #(('a','b'), ('a','b')) -> ('ab', 'ab')
    if all(isinstance(x, str) for x in values):
        return "".join(values)
    tmp = []
    for x in values:
        if isinstance(x, tuple):
            tmp.append(bake_inner(x))
        else:
            tmp.append(x)
    return tuple(tmp)

def flatten(values):
    if isinstance(values, str) or isinstance(values, int):
        yield values
    else:
        for v in values:
            yield from flatten(v)

def bake(values):
    values = bake_inner(values)
    return set(tuple(flatten(values)))
    # values = list(chain.from_iterable(values))

# a = ((1, 2), (3, 4))
# a = ('a')
# print(a, '->', list(flatten(a)))
# exit()

# a = bake([['b', 'a'], ['ba', 'b']])
# assert(a == ['ba', 'bab'])
# assert(bake([['b', 'a'], ['ba', 'b']]) == ['ba', 'bab'])
# assert(bake([['a', 'x', 'b'], ['a', 'y', 'b']]) == ['axb', 'ayb'])
# assert(bake([[['a']], ['b']]) == ['a', 'b'])
# a = ('a',)
# print(a, '->', bake2(a))
# a = ('a','b')
# print(a, '->', bake2(a))

# a = (('a','b'), ('b','a'))
# print(a, '->', bake2(a))

# a = ((('a','b'), ('b','a')), 'c')
# print(a, '->', bake2(a)) # (abc, bac)
# # print(a, '->', bake2(bake2(a))) # (abc, bac)

# a = [((('aa', 'ab'), ('ab', 'aa')), (('bb', 'ab'), ('ab', 'bb'))), ((('aa', 'ba'), ('ba', 'aa')), (('bb', 'ba'), ('ba', 'bb')))]
# print(a, '->', bake2(a))
# exit()
# print(bake( [[ ['ba'], ['bab']], ['xy']] )) # ba or bab or xy
# assert(bake( [[ ['b', 'a'], ['ba', 'b']], ['xy']] ) == ['ba', 'bab', 'xy'])
# exit()

# print( bake([[['a', 'b'], ['a', 'b']], [['b', 'a'], ['b', 'a']]]) )
# assert(bake([[['a', 'b'], ['a', 'b']], [['b', 'a'], ['b', 'a']]]), [['ab', 'ab'], ['ba', 'ba']])
# print(bake([[['a', 'b'], ['a', 'b']]]))
# exit()

contains = defaultdict(set)
for k,v in rules.items():
    flat = flatten(v)
    for x in flat:
        contains[x].add(k)
# for k,v in contains.items():
#     print(k,v)
# exit()

def resolve_rules(rules):
    prev = -1
    while True:
        current = len(seen)
        if prev == current:
            print('Nothing was resolved this iteration!')
            break
        prev = len(seen)

        for key, values in rules.items():
            # print(key, values)
            if key not in seen and is_resolved(values):
                seen.add(key)

                resolved = bake(values)
                rules[key] = resolved

                # print(f'{key} is now resolved {resolved}')
                if key == 0:
                    return resolved
                
                # resolve others who reference key
                for k in contains[key]:
                    v = rules[k]
                    new = set()

                    for option in resolved:
                        new.add(replace(v, match=key, new=option))
                    
                    rules[k] = new


rule = resolve_rules(rules)
# print()
# for k,v in sorted(rules.items()):
#     print(k,v)

# print(seen)
# print("rule0:", rule)
print("rule0 lenght:", len(rule))
# print("rule0 set lenght:", len(set(rule)))
# print("rule1:", rules[1])
print()
tot = 0
for line in lines:
    if line in rule:
        print(f'{line} in rule')
        tot += 1
    else:
        print(f'{line} not in rule')
print(tot)

# print('part1', sum(line == rule for line in lines))

# 201 is too low