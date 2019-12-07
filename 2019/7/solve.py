from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat
from computer import Computer
import queue
from threading import Thread
from collections import deque

# def test_combination_part_1(phase_combination):
#     # phase = deque([1,0,4,3,2])
#     phase = deque(phase_combination)
#     prev_output = 0
#     for i in range(5):
#         computer = Computer(debug=False)
#         computer.load_memory('input.txt')
#         computer.input_queue = deque()

#         computer.input_queue.append(phase.popleft())
#         computer.input_queue.append(prev_output)

#         computer.run()

#         prev_output = computer.output
#         # print("prev_output: ", prev_output)

#     return prev_output

counter = 0

def test_combination(phase_combination):
    global counter
    counter += 1
    computers = []
    phase = deque(phase_combination)
    prev_output = 0

    # init all
    for i in range(5):
        computer = Computer(debug=False)
        computer.load_memory('input.txt')
        computer.output_queue = queue.Queue()
        computer.name = f"{i} run: {counter}"

        computers.append(computer)

    # for prev, current in zip(computers, computer[1:]):
    #     current.input_queue =
    computers[0].input_queue = computers[4].output_queue
    computers[1].input_queue = computers[0].output_queue
    computers[2].input_queue = computers[1].output_queue
    computers[3].input_queue = computers[2].output_queue
    computers[4].input_queue = computers[3].output_queue

    d = computers[0].input_queue.qsize()
    assert d == 0

    for i in range(5):
        computers[i].input_queue.put(phase.popleft())

    computers[0].input_queue.put(0)

    threads = []
    for computer in computers:
        thread = Thread(target = computer.run)
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    return computers[-1].output

# part1
# print(max(test_combination_part_1(p) for p in permutations([4,3,2,1,0])))

# phases = [9,8,7,6,5]
# print(test_combination(phases))

# phases = [9,7,8,5,6]
# print("last: ", test_combination(phases))
# part2
print(max(test_combination(p) for p in permutations([5,6,7,8,9])))