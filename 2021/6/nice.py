from collections import deque

# Inspired by:
# 1. https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnfaisu/?utm_source=share&utm_medium=web2x&context=3
# 2. https://www.reddit.com/r/adventofcode/comments/r9z49j/comment/hnfd2w5/?utm_source=share&utm_medium=web2x&context=3

# (1) was first but (2) was more concise.
# (2) does a rotation on lists manually. So here is a solution using deques with maxsize where we can use the builtin rotate for deques.

# rotate(-1) is not self evident so added a lambda to make it clearer.

data = open('input.txt').read()
fish = deque([data.count(i) for i in '012345678'], maxlen=9)

rotate_left = lambda f: f.rotate(-1)

for _ in range(256):
    rotate_left(fish)
    fish[6] += fish[-1]

print(sum(fish))