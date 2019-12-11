from collections import defaultdict
from computer import Computer
import queue
from threading import Thread

robot_input = queue.Queue()
robot_output = queue.Queue()

# load a computer
computer = Computer(debug=False)
computer.load_memory('input.txt')
computer.output_queue = robot_input
computer.input_queue = robot_output

thread = Thread(target = computer.run)
thread.start()

# data = [line.strip() for line in open('input.txt')]
# data = [int(x) for x in data]

directions = {
    0 : (1, 0), 
    1 : (0, 1),
    2 : (-1, 0),
    3 : (0, -1),
}

# 0 is up
# 1 is right
# 2 is down
# 3 is left
direction = 0

# turn and then move forward once
# when over black computer input should receive 0
# when over white computer input should receive 1

pos = (0, 0)
# default color is black
grid = defaultdict(int)
grid[pos] = 1
painted = set()
while True:

    if computer.abort:
        break
    
    out = grid[pos]
    # print(f"robot giving output: {out}")
    robot_output.put(out)

    color = int(robot_input.get())
    # color = ".#"[color] # 0 is black (.) 1 is white (#)
    # print(f"new color is {color}")

    # print(f"pos {pos} now in {color}")
    grid[pos] = color
    painted.add(pos)

    turn = int(robot_input.get())
    # 0 is turn left, 1 is turn right
    # change it to be -1 and 1
    turn = [-1, 1][turn]


    direction += turn
    # print("turn:", turn, end = " ")
    direction = direction % 4
    # print(f"new direction is {direction}", end = " ")

    change = directions[direction]
    pos = (pos[0] + change[0], pos[1] + change[1])
    # print(f"new pos {pos}")


# part 1
print(len(painted))

# part 2
for y in range(0, 50):
    for x in range(-25, 25):
        color = grid[(x, y)]
        print(".#"[color], end="")
    print()

# BLOZOJLZ
# BLCZCJLZ was right