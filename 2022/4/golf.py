def P(x):l,h=map(int,x.split('-'));return{*range(l,h+1)}
data=[[*map(P,x.split(','))]for x in open('input.txt')]
print(sum(a<=b or b<=a for a,b in data))
print(sum(any(a&b)for a,b in data))
# 192 chars according to vscode on windows.

