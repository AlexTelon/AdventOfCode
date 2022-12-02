from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat, count
import queue
from threading import Thread
from collections import deque
from decimal import Decimal
from fractions import Fraction
import fractions
# import networkx
import string
import operator
import re

from aocd import submit

# nums = '       12 13 a 1'
# nums = re.findall(r'-?\d+', nums)

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

convert = {
    'A': 'rock',
    'B': 'paper',
    'C': 'scissors',
    'X': 'rock',
    'Y': 'paper',
    'Z': 'scissors',
}

def me_won(a, b):
    m = a+b
    if m in ['rockpaper', 'scissorsrock', 'paperscissors']:
        return True
    return False

t = 0
for line in lines:
    elf, me = line.split()
    elf = convert[elf]
    me =  convert[me]
    w = me_won(elf, me)
    t += [' ', 'rock', 'paper','scissors'].index(me)
    if w:
        t += 6
    elif me == elf:
        t += 3
    # print(elf, me, w)

submit(t)