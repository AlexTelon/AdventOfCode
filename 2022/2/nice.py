with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

convert = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win',
}

def lose(a):
    i = ['paper', 'rock', 'scissors'].index(a)
    return ['paper', 'rock', 'scissors', 'paper'][i+1]

def win(a):
    i = ['paper', 'rock', 'scissors'].index(a)
    return ['paper', 'rock', 'scissors'][i-1]

def draw(a):
    return a

def me_won(elf, me):
    return me == win(elf)

score = 0
for line in lines:
    elf, me = line.split()
    elf = convert[elf]
    me  = convert[me]

    if    me == 'lose': me = lose(elf)
    elif  me == 'draw': me = draw(elf)
    else:               me = win(elf)

    score += [' ', 'rock', 'paper','scissors'].index(me)
    if me_won(elf, me):
        score += 6
    elif me == elf:
        score += 3

print(score)