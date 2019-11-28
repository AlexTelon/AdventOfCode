from collections import Counter

with open('input.txt') as f:
    data = f.read()

    floor = 0
    for i, c in enumerate(data):
        if c == '(':
            floor += 1
        else:
            floor -= 1
        if floor == -1:
            print(i+1)
            exit()


# 1794 is too low
# 1795