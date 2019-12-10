# data = [line.split('),') for line in open('result.txt')]
data = open('result.txt').read()
data = eval(data)
print(data)