from itertools import cycle, product
from collections import Counter, defaultdict
from typing import Dict, Tuple


positions = [4, 2] # my input
# positions = [4, 8] # test input

# transform to 0 indexed positions
positions = [p-1 % 10 for p in positions]
scores = [0, 0]

dice = cycle(range(1,101))
rolls = 0
def roll_dice(n):
    global rolls
    rolls += n
    return [next(dice) for _ in range(n)]

done = False
while not done:
    for i in range(2):
        step = sum(roll_dice(3))
        positions[i] = (positions[i] + step) % 10
        scores[i] += positions[i] + 1
        if max(scores) >= 1000:
            done=True
            break

# print('dice rolls:', rolls)
# print('p1 score:', scores[0])
# print('p2 score:', scores[1])
print('part 1', min(scores) * rolls)

# part 2
dice = cycle(range(1,4))

def possible_next_scores(scores: Dict[Tuple[int,int],int]):
    """Update the possible scores after another dice throw."""
    winners = [0, 0]
    possible_steps = [sum(d) for d in product([1,2,3], repeat=3)]
    result = defaultdict(int)
    for (p1, s1, p2, s2), c in scores.items():
        for steps, cc1 in Counter(possible_steps).items():
            _p1 = (p1 + steps) % 10
            _s1 = s1 + (_p1 + 1)
            if _s1 >= 21:
                # if p1 won then count em but dont add state to dictionary. no need to simulate those further.
                # print(f'p1 won {c}*{cc1} (steps={steps}, score={_s1})')
                winners[0] += c*cc1
            else:
                for steps, cc2 in Counter(possible_steps).items():
                    _p2 = (p2 + steps) % 10
                    _s2 = s2 + (_p2 + 1)
                    if _s2 >= 21:
                        # if p2 won then count em but dont add state to dictionary. no need to simulate those further.
                        winners[1] += c*cc2*cc1
                    else:
                        # only if nobody wins will we add the state to result.
                        result[(_p1, _s1, _p2, _s2)] += c*cc1*cc2

    return result, winners

# map the current state of the board to how many ways to get here.
scores = {(positions[0], 0, positions[1], 0): 1}
winners = [0, 0]

done = False
while not done:
    scores, new_winners = possible_next_scores(scores)
    winners[0] += new_winners[0]
    winners[1] += new_winners[1]
    # print('winners', winners)
    # print('scores', len(scores))
    if not any(s for s in scores):
        break

# print(winners)
# print(scores)

# tests when verifying against sample input
# if winners == [444356092776315, 341960390180808]:
#     print('done!')
#     exit()

# print(f"{(winners[0] / 444356092776315):.8%}")
# print(f"{(winners[1] / 341960390180808):.8%}")

print('p2 winner universes', max(winners))