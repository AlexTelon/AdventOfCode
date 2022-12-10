from itertools import accumulate, tee
import re
import textwrap

xs = map(int, re.sub(pattern=r'[noop|addx]', repl='0', string=open('input.txt').read()).split())

part1, part2 = 0, ''
for i, x in enumerate(accumulate(xs, initial=1), start=1):
    part1 += i*x if i%40==20 else 0
    part2 += '#' if (i-1)%40 in [x-1,x,x+1] else ' '

print(part1)
size = 5
# Make it wider and wrap.
text = textwrap.wrap(''.join(c*size for c in part2), width=40*size)
# Make it higher.
print('\n'.join(map('\n'.join,zip(*tee(text, size)))))