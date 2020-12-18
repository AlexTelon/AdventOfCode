from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat, count
from os import kill
import queue
from threading import Thread
from collections import deque
from decimal import Decimal
from fractions import Fraction
import fractions
# import networkx
import string
import operator

# product('ABCD', repeat=2)                 -> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                   -> AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                   -> AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)  -> AA AB AC AD BB BC BD CC CD DD

# if you have multiple lines of stuff in groups, and groups seperated by empty lines.
# groups = open(0).read().split("\n\n")
# for group in groups:
#     for line in group.splitlines():
#         print(line)

# lines = open('sample.txt').read().splitlines()
lines = open(0).read().splitlines()
lines = [line for line in lines if line[0] != '#']

op = {
    '*': operator.mul,
    '+' : operator.add,
}

class Tree:
    def __init__(self):
        self.left = None
        self.right = None
        self.this = None

    def __repr__(self):
        return f"{self.left if self.left is not None else ''} {self.data} {self.right if self.right is not None else ''}"

def step(parts):
    first = parts.popleft()
    if first[0] == '(':
        # go until next ')'. but what if there are more '(' on the way?
        # parts.appendleft(first)
        count = {'(': first.count('('), ')': 0}
        deeper = deque([first.replace('(', '', 1)])
        while count['('] != count[')']:
            new = parts.popleft()
            count['('] += new.count('(')
            count[')'] += new.count(')')
            deeper.append(new)
        
        # remove last )
        last = deeper.pop()
        deeper.append(last.replace(')', '', 1))
        first = parser(deeper)
    return first, parts

def parser(parts):
    # result = Tree()
    # print(f'parser: {parts}')
    if isinstance(parts, Tree):
        return parts
    if isinstance(parts, str):
        node = Tree()
        # node.data = parts
        node.data = int(parts.replace('(', '').replace(')', ''))
        return node
    if len(parts) == 1:
        # node = Tree()
        # node.data = parts.pop()
        return parts[0]
    if len(parts) >= 3:
        left = parts.popleft()
        if isinstance(left, str):
            parts.appendleft(left)
            left, parts = step(parts)

        operator = parts.popleft()

        right = parts.popleft()
        if isinstance(right, str):
            parts.appendleft(right)
            right, parts = step(parts)

        node = Tree()
        node.left = parser(left)
        node.data = operator
        node.right = parser(right)
        # parts = deque([node, parts])
        parts.appendleft(node)
        return parser(parts)
    assert False

def evaluate(tree):
    if tree.left is None and tree.right is None:
        return tree.data
    operator = op[tree.data]
    left = evaluate(tree.left)
    right = evaluate(tree.right)
    # print(f'eval: {left} {operator} {right}')
    res = operator(left, right)
    print(tree, '=', res)
    return res

tot = 0
for line in lines:
    # line = line[::-1]
    print("line:", line)
    tree = parser(deque(line.split()))
    print("tree:", tree)
    value = evaluate(tree)
    print(value)
    print()
    tot += value
print(tot)


# 1038000279625 is too low.