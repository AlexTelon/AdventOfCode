
data = [tuple(map(int, line.strip().split('x'))) for line in open('input.txt')]

total = 0
for length, width, height in data:
    surface_area = 2*length*width + 2*width*height + 2*height*length
    # slack is the area of the smallest side
    slack = (length * width * height) // max(length, width, height)

    total += surface_area + slack

print(total)