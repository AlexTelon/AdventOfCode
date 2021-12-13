coords, _folds = open('input.txt').read().split('\n\n')

grid = {tuple(map(int,cord.split(','))) for cord in coords.splitlines()}

folds = []
for line in _folds.splitlines():
    direction, value = line.replace('fold along ', '').split('=')
    folds.append((direction, int(value)))

def debug_draw():
    # Now hardcoded ranges to display the letters at the end.
    for y in range(6):
        for x in range(40):
            print(end='#' if (x,y) in grid else ' ')
        print()

first = True
for direction, value in folds:
    if direction == 'x':
        for x,y in grid.copy():
            if x > value:
                grid.add((value - (x - value), y))
                grid.remove((x,y))
    else:
        for x,y in grid.copy():
            if y > value:
                grid.add((x, value - (y - value)))
                grid.remove((x,y))

    if first:
        print('p1', len(grid))
        first = False

# The ans is drawn to the screen.
debug_draw()
