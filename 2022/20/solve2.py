
nums = list(enumerate(map(int,open('sample.txt').read().splitlines())))
# nums = list(enumerate(map(int,open('in.txt').read().splitlines())))
# nums = list(enumerate(map(int,open('sample2.txt').read().splitlines())))
# print([v for i,v in nums])
print()
n = len(nums)

for pair in nums[::]:
    _, num = pair

    i = nums.index(pair)

    j = i + num
    if j <= 0: j -= 1
    if j > n: j += 1 
    j = j % n

    print(f'{num=} to {j}')

    nums.remove(pair)
    nums.insert(j, pair)
    print(*[v for i,v in nums])

print()
print('final')
print(*[v for i,v in nums])

nums = [v for i,v in nums]
# Then, the grove coordinates can be found by looking at the 1000th, 2000th, and 3000th n
m = nums.index(0)
print('0 index', m)
a = nums[(m+1000) % n]
b = nums[(m+2000) % n]
c = nums[(m+3000) % n]
print(a,b,c)
print(sum([a,b,c]))

#  not 4706, too high