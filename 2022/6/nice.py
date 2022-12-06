line = open('input.txt').read()

def solve(size):
    for i in range(size, len(line)):
        part = line[i-size:i]
        if len(set(part)) == size:
            return i

print(solve(4))
print(solve(14))