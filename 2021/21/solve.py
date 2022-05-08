from itertools import cycle


positions = [4, 2]
# positions = [4, 8]
# TODO
positions = [p-1 % 10 for p in positions]
scores = [0, 0]

dice = cycle(range(1,101))

rolls = 0

def roll_dice(n):
    global rolls
    rolls += n
    return [next(dice) for i in range(n)]


done = False
while not done:
    for i in range(2):
        step = sum(roll_dice(3))
        positions[i] = (positions[i] + step) % 10
        scores[i] += positions[i] + 1
        if max(scores) >= 1000:
            done=True
            break

print('dice rolls:', rolls)
print('p1 score:', scores[0])
print('p2 score:', scores[1])

print('part 1', min(scores) * rolls)