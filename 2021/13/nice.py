coords, folds = open('input.txt').read().split('\n\n')

grid = {tuple(map(int,cord.split(','))) for cord in coords.splitlines()}
folds = [line.replace('fold along ', '').split('=') for line in folds.splitlines()]
folds = [(d, int(value)) for d, value in folds]

# Generic fold along one axis.
fold = lambda a, fold: fold - abs(a - fold)

# Perform all folds.
for direction, edge in folds:
    if direction == 'x':
        transform = lambda x,y: (fold(x, edge), y)
    else:
        transform = lambda x,y: (x, fold(y, edge))

    grid = {transform(x,y) for x,y in grid}

# The ans is drawn to the screen.
for y in range(6):
    for x in range(40):
        print(end='#' if (x,y) in grid else ' ')
    print()