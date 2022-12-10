with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

program = ['i=1', 'x=1']
for line in lines:
    if line == 'noop':
        program.append('i+=1')
    else:
        d = line.split()[-1]
        program.append('i+=1')
        program.append(f'i+=1;x+={d}')

p1 = []
for instruction in program:
    exec(instruction)
    exec('if i == 20 or ((i - 20) % 40 == 0):p1 += [i*x]')

print(p1, sum(p1))
