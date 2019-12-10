def slow(a , b):
    # check if we by repeating b can build a
    if b[0] == 0 and b[1] == 0:
        return a[0] == 0 and b[0] == 0

    x_min = 0
    x_max = 100
    if b[0] < 0:
        x_max = -x_max
    
    y_min = 0
    y_max = 100
    if b[1] < 0:
        y_max = -y_max


    if b[0] == 0:
        x = 0
        for y in range(y_min, y_max, b[1]):
            if a == (x, y):
                return True
        return False

    if b[1] == 0:
        y = 0
        for x in range(x_min, x_max, b[0]):
            if a == (x, y):
                return True
        return False

    for x, y in zip(range(x_min, x_max, b[0]), range(y_min, y_max, b[1])):
        if a == (x, y):
            return True

    return False


def fast(a, b):
    pass

# check if slow and fast always give same results