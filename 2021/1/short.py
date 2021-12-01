l=[*map(int,open('input.txt').read().splitlines())]
print(sum(b>a for a,b in zip(l,l[1:])))
print(sum(sum(l[i-2:i+1])>sum(l[i-3:i])for i in range(3,len(l))))