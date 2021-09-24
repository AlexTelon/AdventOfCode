lines = open('input.txt').read().splitlines()
# Wanted to try the same type of solution after seeing https://github.com/sophiebits/adventofcode/blob/main/2020/day12.py
# Less overhead this way..


x, y = 0, 0
xw, yw = 10, 1
dir = 90

for line in lines:
    c, magnitude = line[0], int(line[1:])
    print(c, magnitude)

    if c == 'R':
        while magnitude > 0:
            xw, yw = yw, -xw
            magnitude -= 90
    if c == 'L':
        while magnitude > 0:
            xw, yw = -yw, xw
            magnitude -= 90
    if c == 'N':
        yw += magnitude
    if c == 'S':
        yw -= magnitude
    if c == 'E':
        xw += magnitude
    if c == 'W':
        xw -= magnitude
    if c == 'F':
        x += xw * magnitude
        y += yw * magnitude
    
    print("pos", x,y, 'way', xw, yw)

print("FINAL")
print("pos", x,y, 'way', xw, yw)
print(abs(x) + abs(y))