with open('input.txt', 'r') as f:
    l = f.read()

p1 = 0
for x in zip(l,l[1:],l[2:],l[3:]):
    p1 += 1
    if len(set(x)) == 4:
        print('p1', p1+3)
        break

p2 = 0
for x in zip(l,l[1:],l[2:],l[3:],l[4:],l[5:],l[6:],l[7:],l[8:],l[9:],l[10:],l[11:],l[12:],l[13:]):
    p2 += 1
    if len(set(x)) == 14:
        print('p2', p2+13)
        break