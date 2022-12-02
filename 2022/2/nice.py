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

def lose_to(a):
    i = ['paper', 'rock', 'scissors'].index(a)
    return ['paper', 'rock', 'scissors', 'paper'][i+1]

def win_to(a):
    i = ['paper', 'rock', 'scissors'].index(a)
    return ['paper', 'rock', 'scissors'][i-1]

def draw_to(a):
    return a

def me_won(elf, me):
    return me == win_to(elf)

score = 0
for line in lines:
    elf, me = line.split()
    elf = convert[elf]
    me  = convert[me]

    if    me == 'lose': me = lose_to(elf)
    elif  me == 'draw': me = draw_to(elf)
    else:               me = win_to(elf)

    score += [' ', 'rock', 'paper','scissors'].index(me)
    if me_won(elf, me):
        score += 6
    elif me == elf:
        score += 3

print(score)