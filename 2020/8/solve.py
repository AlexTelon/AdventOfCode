from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat
import queue
from threading import Thread
from collections import deque
from decimal import Decimal
from fractions import Fraction
import fractions
import networkx
import string
import operator
## read file line by line
# some code that reads a file line by line
lines = open('input.txt').read().splitlines()
instructions = [line.split() for line in lines]

accumulator = 0
pointer = 0
visited = set()

def acc(inc):
    global accumulator
    accumulator += inc

def jmp(rel):
    global pointer
    pointer += rel
    if pointer not in visited:
        visited.add(pointer)
    else:
        print(f'visited {pointer} a second time!')
        print('part1', accumulator)
        exit()

def nop(num):
    pass

op_codes = {
    'acc': acc,
    'jmp' : jmp,
    'nop' : nop,
}



# for op, num in instructions:
while True:
    op, num = instructions[pointer]
    num = int(num)
    print(pointer, op, num)
    op_codes[op](num)
    if op != 'jmp':
        op_codes['jmp'](1)

    
    # print(accumulator, pointer)
# jmp relative +2 skips next instruction
# jmp relative -1 go to 1 above it

#1589