content = open('input.txt').read()
content = content.replace('noop','i+=1')
content = content.replace('addx','i+=1\ni+=1;x+=')
lines = content.splitlines()

i=1
x=1
display = ['_' for _ in range(40*6)]
p1 = 0
for instruction in lines:
    display[i-1] = '#' if ((i-1) % 40) in [x-1, x, x+1] else ' '
    exec(instruction)
    if i == 20 or ((i - 20) % 40 == 0):
        p1 += i*x

print('p1', p1)
for i, c in enumerate(display):
    print(end=c)
    if i % 40 == 39:
        print()