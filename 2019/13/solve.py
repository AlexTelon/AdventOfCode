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

# load a computer
computer = Computer(debug=False)
computer.load_memory('input.txt')
computer.output_queue = computer_output
computer.input_queue = computer_input

thread = Thread(target = computer.run)
thread.start()


grid = defaultdict(int)
SCORE = 0
ball_pos, player_pos = (0, 0), (0, 0)

def update_gameboard_loop():
    global SCORE, ball_pos, player_pos
    while True:
        # not sure why this breaks out one step too early and results in the wrong answer..
        # if computer.abort:
        #     break
        X = int(computer_output.get())
        Y = int(computer_output.get())
        pos = (X, Y)
        if pos == (-1, 0):
            SCORE = int(computer_output.get())
            print(f"SCORE: {SCORE}")
        else:
            ID = int(computer_output.get())
            grid[pos] = ID

            if ID == 3:
                player_pos = pos
            elif ID == 4:
                ball_pos = pos



def draw_screen():
    for y in range(0, 20):
        for x in range(0, 48):
            print(" |#-*"[grid[(x, y)]], end = "")
        print()


thread = Thread(target = update_gameboard_loop)
thread.start()

while True:

    if computer.abort:
        break

    if computer.waiting_for_input:
        draw_screen()
        # joystick (if you want to run it manually)
        # import msvcrt
        # input_char = msvcrt.getch().decode("utf-8").lower()
        # direction = 0 if input_char == 's' else -1 if input_char == 'a' else 1

        # Run automatically
        if ball_pos[0] > player_pos[0]:
            direction = 1
        elif ball_pos[0] < player_pos[0]:
            direction = -1
        else:
            direction = 0 

        computer_input.put(direction)

   

# part 1
# print("part1: ", len([v for pos, v in grid.items() if v == 2]))

# part 2
print(f"SCORE (at end): {SCORE}")
