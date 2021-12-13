# Input consists of lines of coordinates followed by lines of folds.
coords, folds = open('input.txt').read().split('\n\n')

# Defines a generic fold along one axis.
fold = lambda a, fold: fold - abs(a - fold)

# Create all folds. Each fold is defined by a function that can perform the fold on any (x,y) coordinate.
folds = [line.replace('fold along ', '').split('=') for line in folds.splitlines()]
folds = [
    [
        lambda x,y,edge=int(edge): (x, fold(y, edge)),
        lambda x,y,edge=int(edge): (fold(x, edge), y)
    ][d=='x']
    for d, edge in folds]

# Initial grid.
grid = {tuple(map(int,cord.split(','))) for cord in coords.splitlines()}

# Perform all folds. Update the grid as we go.
[grid := {transform(x,y) for x,y in grid} for transform in folds]

# The answer is drawn to the screen.
for y in range(6):
    for x in range(40):
        print(end='#' if (x,y) in grid else ' ')
    print()