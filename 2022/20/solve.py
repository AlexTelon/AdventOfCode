def solve(nums):
    n = len(nums)
    pairs = nums[::]

    for _ in range(10):
        for pair in pairs:
            _, num = pair
            i = nums.index(pair)

            if num != 0:
                j = ((i + num - 1) % (n - 1)) + 1
            else:
                j = i

            nums.remove(pair)
            nums.insert(j, pair)
    return [v for _,v in nums]

nums = solve(list(enumerate(x * 811589153 for x in map(int,open('in.txt').read().splitlines()))))

n = len(nums)
m = nums.index(0)
a = nums[(m+1000) % n]
b = nums[(m+2000) % n]
c = nums[(m+3000) % n]
print(sum([a,b,c]))