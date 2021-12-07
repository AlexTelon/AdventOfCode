nums = list(map(int,open('input.txt').read().split(',')))
# p1
# def dist(a, b):
#     return abs(a-b)

def dist(a, b):
    return sum(range(1, abs(a-b)+1))

print(min(sum(dist(num, other) for other in nums) for num in nums))