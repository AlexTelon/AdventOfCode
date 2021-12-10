from collections import deque

lines = open('input.txt').read().splitlines()

scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}
scores2 = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4,
}
OPENERS = '([{<'

def to_close(c):
    t = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>',
    }
    return t[c]

def to_open(c):
    t = {
        ')': '(',
        ']': '[',
        '}': '{',
        '>': '<',
    }
    return t[c]

p1 = 0
p2_scores = []
for line in lines:    
    stack = deque()

    syntax_err = False
    for c in line:
        if c in OPENERS:
            stack.append(c)
        else:
            # If current char closes a pair, then on top of the stack we should find the corresponding opener!
            out = stack.pop()
        
            if to_close(out) != c:
                # syntax error!
                p1 += scores[c]
                syntax_err = True
                continue
    
    if len(stack) != 0 and not syntax_err:
        # Incomplete if there are still things left in the stack without syntax error abort.
        
        # How to apply a fix.
        fix = [to_close(c) for c in reversed(stack)]

        # Scoore of said fix.
        score = 0
        for i, c in enumerate(fix):
            score *= 5
            score += scores2[c]

        p2_scores.append(score)

print('p1', p1)
n = len(p2_scores)
print('p2', sorted(p2_scores)[n//2])