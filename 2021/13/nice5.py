from functools import partial, reduce
# Input consists of lines of coordinates followed by lines of folds.
coords, folds = open('input.txt').read().split('\n\n')

# Defines a generic fold along one axis.
fold = lambda a, fold: fold - abs(a - fold)
def fold_y(x, y, edge):
    return (x, fold(y, edge))

def fold_x(x, y, edge):
    return (fold(x, edge), y)

# Create all folds. Each fold is defined by a function that can perform the fold on any (x,y) coordinate.
folds = [line.replace('fold along ', '').split('=') for line in folds.splitlines()]
folds = [[partial(fold_y,edge=int(edge)), partial(fold_x,edge=int(edge))][d=='x'] for d, edge in folds]

# Initial grid.
coords = {tuple(map(int,cord.split(','))) for cord in coords.splitlines()}

# Create one function that performs all transforms for a given position.
transform = reduce(lambda f, ff: lambda x,y: ff(*f(x,y)), folds)

# Apply all transformations point for point.
grid = {transform(x,y) for x,y in coords}

# The answer is drawn to the screen.
for y in range(6):
    for x in range(40):
        print(end='#' if (x,y) in grid else ' ')
    print()