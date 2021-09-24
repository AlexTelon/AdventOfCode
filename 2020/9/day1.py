lines = open('input.txt').read().splitlines()
nums = [int(line) for line in lines]

goal = 2020

found = set()

def find_goal(goal):
    global found
    for num in nums:
        if goal - num in found:
            return (num, (goal - num))
        else:
            found.add(num)
    
    return False

for num in nums:
    new_goal = 2020 - num
    if find_goal(new_goal):
        #print('sum', sum(find_goal(new_goal), (new_goal)))
        #print(a, b, num)
        a, b = find_goal(new_goal)
        print(a * b * num)