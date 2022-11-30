with open('input.txt', 'r') as f:
    data = f.read().splitlines()

# 3-11 z: zzzzzdzzzzlzz
p1 = 0
p2 = 0
for line in data:
    a, password = line.split(':')
    password = password.strip()
    lohi, char = a.split()
    lo, hi = lohi.split('-')
    lo = int(lo) - 1
    hi = int(hi) - 1
    # p1
    p1 += password.count(char) in range(lo,hi+1)
    # p2
    password = (password[lo] + password[hi])
    p2 += password.count(char) == 1
print(p1)
print(p2)


