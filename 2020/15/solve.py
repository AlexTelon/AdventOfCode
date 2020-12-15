from collections import defaultdict, deque
from itertools import count

memory = defaultdict(tuple)
nums = [2,0,1,9,5,19]
# nums = [1,3,2]
# nums = [3,1,2]

prev = nums[0]
for i, num in enumerate(nums):
    memory[num] = (i, )
    # print(f'turn {i+1}: just say {num}')
    prev = num


def update_memory(say):
    global memory
    if say in memory:
        if len(memory[say]) == 2:
            memory[say] = (memory[say][1], i)
        else:
            memory[say] = (memory[say][0], i)
    else:
        memory[say] = (i,)


for i in count(len(nums)):
    if prev in memory and len(memory[prev]) == 1:
        say = 0
        # print(f'turn {i+1}: memory[{prev}] = {memory[prev]} just say {say}')
        update_memory(say)
        prev = say
    else:
        say = memory[prev][1] - memory[prev][0]
        # print(f'turn {i+1}: prev is {prev}, {memory[prev]} say {say}')
        update_memory(say)        
        prev = say
    
    # if i+1 == 2020:
    #     print("part1", say)
    #     # break
    if i == 29_999_999:
        print("part1", say)
        break
