from collections import defaultdict, deque
from itertools import count

from functools import partial

# Partial can be used to create new functions.
# buffer is now a callable thay calls deque with maxlen=2.
buffer = partial(deque, maxlen=2)
# Defaultdict needs a callable without args. Hence partial above.
memory = defaultdict(buffer)

nums = [2,0,1,9,5,19]

prev = nums[0]
for i, num in enumerate(nums):
    memory[num].append(i)
    prev = num

for i in count(len(nums)):
    if len(memory[prev]) == 1:
        # Last time it was the first time. (only 1 in memory).
        say = 0
        # print(f'turn {i+1}: memory[{prev}] = {memory[prev]} just say {say}')
    else:
        say = memory[prev][1] - memory[prev][0]
        # print(f'turn {i+1}: prev is {prev}, {memory[prev]} say {say}')

    memory[say].append(i)
    prev = say

    if i == 2019:
        print("part1 2020:", say)
        # break
    if i == 29_999_999:
        print("part1 30_000_000:", say)
        break
