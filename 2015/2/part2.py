data = [list(map(int, line.strip().split('x'))) for line in open('input.txt')]

total = 0
for lenghts in data:
    a, b, c = sorted(lenghts)

    # slack is the area of the smallest side (divide away the largest length and you get the two smallest only)
    permiter_around_smallest = 2 * a + 2 * b
    volume = a * b * c

    total += permiter_around_smallest + volume

print(total)