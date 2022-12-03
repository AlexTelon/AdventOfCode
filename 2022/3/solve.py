import string

letters = string.ascii_lowercase + string.ascii_uppercase
def prio(c):
    return letters.index(c) + 1

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

t = 0
stuff = []
for line in lines:
    # split in two halves.
    a,b = line[:len(line)//2], line[len(line)//2:]
    common = set(a).intersection(b)
    stuff.append(''.join(common))

# p1
print(sum(map(prio, stuff)))

stuff = []
for i in range(0,len(lines),3):
    a,b,c = lines[i:i+3]
    common = set(a).intersection(b).intersection(c)
    stuff.append(''.join(common))

# p2
print(sum(map(prio, stuff)))
