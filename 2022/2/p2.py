from aocd import submit

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

convert = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

def me_won(a, b):
    m = a+b
    if m in ['rockpaper', 'scissorsrock', 'paperscissors']:
        return True
    return False

t = 0
for line in lines:
    elf, me = line.split()
    elf = convert[elf]
    if me == 'X':
        # lose
        if elf == 'rock':
            me = 'scissors'
        elif elf == 'paper':
            me = 'rock'
        else: 
            me = 'paper'
    elif me == 'Y':
        # draw
        me = elf
    else:
        if elf == 'scissors':
            me = 'rock'
        elif elf == 'rock':
            me = 'paper'
        else: 
            me = 'scissors'
    w = me_won(elf, me)
    t += [' ', 'rock', 'paper','scissors'].index(me)
    if w:
        t += 6
    elif me == elf:
        t += 3

submit(t)