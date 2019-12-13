from collections import defaultdict, Counter, namedtuple
import itertools
from itertools import product, permutations, combinations, repeat
# from computer import Computer
import queue
from threading import Thread
from collections import deque
from decimal import Decimal
import operator
from pprint import pprint
from functools import reduce
from math import gcd

from collections import defaultdict
from computer import Computer
import queue
from threading import Thread

computer_output = queue.Queue()
computer_input = queue.Queue()

# # put coint (part 2)
# computer_input.put(2)

# load a computer
computer = Computer(debug=False)
computer.load_memory('input.txt')
computer.output_queue = computer_output
computer.input_queue = computer_input

thread = Thread(target = computer.run)
thread.start()



pos = (0, 0)
grid = defaultdict(int)
grid[pos] = 1
painted = set()
while True:

    if computer.abort:
        break
    
    out = grid[pos]
    # print(f"robot giving output: {out}")
    # computer_input.put(out)

    X = int(computer_output.get())
    Y = int(computer_output.get())
    ID = int(computer_output.get())
    pos = (X, Y)
    
    # color = ".#"[color] # 0 is black (.) 1 is white (#)
    # print(f"new color is {color}")

    # print(f"pos {pos} now in {color}")
    grid[pos] = ID
   

# part 1
print(len([v for pos, v in grid.items() if v == 2]))

# part 2

# for y in range(0, 50):
#     for x in range(-25, 25):
#         color = grid[(x, y)]
#         print(".#"[color], end="")
#     print()
