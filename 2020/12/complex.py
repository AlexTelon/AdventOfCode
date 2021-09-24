lines = open('input.txt').read().splitlines()
# Inspired by reddit

pos = complex(0,0)
waypoint = complex(10,1)

for line in lines:
    c, magnitude = line[0], int(line[1:])
    print(c, magnitude)

    if c == 'N':
        waypoint += complex(0, magnitude)
    if c == 'S':
        waypoint += complex(0, -magnitude)
    if c == 'E':
        waypoint += complex(magnitude, 0)
    if c == 'W':
        waypoint += complex(-magnitude, 0)
    
    if c == 'R':
        while magnitude > 0:
            waypoint *= complex(0, -1)
            magnitude -= 90
    if c == 'L':
        while magnitude > 0:
            waypoint *= complex(0, 1)
            magnitude -= 90
    
    if c == 'F':
        pos += waypoint * magnitude
    print(pos, "way", waypoint)

print(int(abs(pos.real) + abs(pos.imag)))