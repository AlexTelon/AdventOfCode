from collections import defaultdict
thing = defaultdict(set)

p2 = 0
for line in open('input.txt').read().splitlines():
    left, right = line.split('|')
    lenghts = {len(s): set(s) for s in left.split()}

    _1 = lenghts[2]
    _4 = lenghts[4]

    n = ''
    for o in map(set, right.split()):
        match len(o), len(o & _4), len(o & _1):
            case 2,_,_: n += '1'; thing['1'].add((len(o), len(o & _4), len(o & _1)))
            case 3,_,_: n += '7'; thing['7'].add((len(o), len(o & _4), len(o & _1)))
            case 4,_,_: n += '4'; thing['4'].add((len(o), len(o & _4), len(o & _1)))
            case 7,_,_: n += '8'; thing['8'].add((len(o), len(o & _4), len(o & _1)))
            case 5,2,_: n += '2'; thing['2'].add((len(o), len(o & _4), len(o & _1)))
            case 5,3,1: n += '5'; thing['5'].add((len(o), len(o & _4), len(o & _1)))
            case 5,3,2: n += '3'; thing['3'].add((len(o), len(o & _4), len(o & _1)))
            case 6,4,_: n += '9'; thing['9'].add((len(o), len(o & _4), len(o & _1)))
            case 6,3,1: n += '6'; thing['6'].add((len(o), len(o & _4), len(o & _1)))
            case 6,3,2: n += '0'; thing['0'].add((len(o), len(o & _4), len(o & _1)))

    p2 += int(n)

print('p1', p2)

print()
import math
for k,v in thing.items():
    print(k, v, math.prod(next(iter(v))))


# print(k, v, math.prod(next(iter(v))))
# 5 {(5, 3, 1)} 15
# 6 {(6, 3, 1)} 18
# 3 {(5, 3, 2)} 30
# 4 {(4, 4, 2)} 32
# 1 {(2, 2, 2)} 8
# 0 {(6, 3, 2)} 36
# 2 {(5, 2, 1)} 10
# 9 {(6, 4, 2)} 48
# 7 {(3, 2, 2)} 12
# 8 {(7, 4, 2)} 56
