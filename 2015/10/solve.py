from itertools import groupby
number = '3113322113'
# for i in range(40): # (part 1)
for i in range(50):
    next_number = ''
    for k,v in groupby(number):
        num = k
        count = len(list(v))
        next_number += (f'{count}{num}')
    number = next_number
# print(number)
print(len(number))
# part 1 04:15
# part 5 05:10