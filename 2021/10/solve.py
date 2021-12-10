from collections import deque

lines = open('input.txt').read().splitlines()

OPENERS = '([{<'
to_close = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>',
}
scores = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137,
}

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
        
            syntax_err = to_close[out] != c
            if syntax_err:
                p1 += scores[c]
                break
    
    incomplete = len(stack) > 0 and not syntax_err
    if incomplete:
        # How to apply a fix.
        fix = [to_close[c] for c in reversed(stack)]

        # Score of said fix.
        score = 0
        for c in fix:
            score *= 5
            score += ' )]}>'.index(c)
        p2_scores.append(score)

print('p1', p1)
n = len(p2_scores)
print('p2', sorted(p2_scores)[n//2])