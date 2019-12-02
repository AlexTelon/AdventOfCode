import collections
import itertools

data = [list(map(int, line.split(','))) for line in open('input.txt')][0]

def add(a, b, c):
    global data
    data[c] = (data[a] + data[b])

def multiply(a, b, c):
    global data
    data[c] = (data[a] * data[b])

def halt(*args):
    print(data)
    print(data[0])
    exit()

op_codes = {
    1: add,
    2: multiply,
    99: halt,
}

pc = 0
while True:
    op = data[pc]
    args = data[pc+1:pc+4]
    op_codes[op](*args)
    pc += 4

