from fractions import Fraction
import math
from math import lcm, gcd
from itertools import count

lines = open(0).read().splitlines()
# for line in lines:
#     print(line)
part_one = True
if part_one:
    goal = int(lines[0])
    busses = list(map(int,lines[1].replace('x', "-1").split(',')))
    # busses = list(map(int,lines[1].replace('x,', "").split(',')))

    print(goal, busses)

    stuff = [goal // buss for buss in busses]

    lowest = math.inf
    buss_id = -1

    for buss in busses:
        if buss == -1:
            continue
        tmp = 0
        while tmp < goal:
            tmp += buss

        if tmp < lowest:
            lowest = min(lowest, tmp)
            buss_id = buss

    wait = lowest - goal
    print("part1", buss_id * wait)
    print()
exit()

# def lcm(a, b):
#     return abs(a*b) // math.gcd(a, b)

# part 2
# print('largest_busss', step_size)
# print('lcm', math.lcm(*busses))
# start = 0
# for a,b in zip(busses, busses[1:]):
#     A, B = 0, 0
#     steps = 0
#     while A != B + 1:
#         A += a
#         B += b
#         steps += 1
#     print(A, B, steps)
#     break

busses = lines[1].split(',')
busses = [(int(x),i) for i,x in enumerate(busses) if x != "x"]
print(busses)
def quota(a,b):
    delta = b[1] - a[1]
    a = a[0]
    b = b[0]
    quota = (b - delta) / a
    return quota

def iterations(a,b):
    # meta_i = 0
    delta = b[1] - a[1]
    a = a[0]
    b = b[0]
    seen = set()
    for i in count(1):
        A = a*i
        B = b*i
        seen.add(B)
        # print(A, B)
        if A + delta in seen:
            # meta_i += 1
            # print(A, A + delta)
            # print(Fraction(i, (A + delta) // b), A, A+delta)
            # if meta_i > 150:
            #     return
            return (i, (A + delta) // b)

quotas = []
first = busses[0]
iters = []
for current in busses[1:]:
    # q = quota(first,current)
    # print(first, current, q, Fraction(q))
    i = iterations(first,current)
    print(first, current, i, 'iterations')
    iters.append(i)
    # quotas.append(Fraction(q))

print(iters)
fracs = [Fraction(b,a) for a,b in iters]
first_iters = [1] + [a for a,b in iters]
other_iters = [1] + [b for a,b in iters]
print(first_iters)
print(other_iters)
lcm_iters = lcm(*first_iters)
all_iterations = [lcm_iters] + [float(f * lcm_iters) for f in fracs]
print(all_iterations)
print('test')
print([x * busses[i][0] for i,x in enumerate(all_iterations)])

exit()
iteration_steps_first = lcm_iters
print("number of iterations:", lcm_iters, "for the first value")
print("number of iterations:", other_iters[1], "for the second value")

print([value * iteration_steps_first * other_iters[i] // first_iters[i] for i, (value, diff) in enumerate(busses)])
# print([value * iteration_steps_first for i, (value, diff) in enumerate(busses)])
# for i in count(1):
#     print([value * iteration_steps * i for value, diff in busses])

# print(lcm(*[value * iteration_steps for value, diff in busses]))
exit()
# for a,b in zip(busses, busses[1:]):
#     q = quota(a,b)
#     print(a,b, q, Fraction(q))
#     quotas.append(Fraction(q))

print(quotas)
numerators = [x.numerator for x in quotas]
denominators = [x.denominator for x in quotas]
# common_gcd = gcd(*denominators)
# print('gcd:', common_gcd)

# now_as_ints = [x * common_gcd for x in numerators]
# print(lcm(*now_as_ints) // common_gcd)

multiple = lcm(*denominators)
print(multiple)
ints = [multiple * x for x in quotas]
print(ints)
print([x.numerator for x in ints])
divisor = gcd(*[x.numerator for x in ints])
# divisor = gcd(*numerators)
print(divisor)

final_numbers = [int(x / divisor) for x in ints]
print(final_numbers)
print([x // denominators[i] for i, x in enumerate(final_numbers)])





# print(lcm(*quotas))

# a = busses[0]
# b = busses[1]
# print(a,b)
# print()
for q in quotas:
    for i in range(1, 10):
        if float(q * i).is_integer():
            print(float(q), i, "iterations")

# q = quotas[0]
# print(float(q))
# print(quotas[0])