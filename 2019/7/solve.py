from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat
from computer import Computer
import queue
from threading import Thread
from collections import deque

# Does not work anymore after I changed things for part2.
# def test_combination_part_1(phase_combination):
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

#     return prev_output

debug_counter = 0

def test_combination(phase_combination):
    global debug_counter
    debug_counter += 1

    computers = []
    phase = deque(phase_combination)

    # Initiaize the computers.
    for i in range(5):
        computer = Computer(debug=False)
        computer.load_memory('input.txt')
        computer.output_queue = queue.Queue()
        computer.name = f"{i} run: {debug_counter}"

        computers.append(computer)

    # TODO async await instead?
    # TODO generators instead?

    for i in range(5):
        computers[i].input_queue = computers[i - 1].output_queue
        computers[i].input_queue.put(phase.popleft())

    # Once all computers have gotten their phase nr first they all shall receive input form the previous one.
    # However we must initialize the first one with 0.
    computers[0].input_queue.put(0)

    threads = []
    for computer in computers:
        thread = Thread(target = computer.run)
        threads.append(thread)
        thread.start()


    for thread in threads:
        thread.join()

    return computers[-1].output

# print("part1: ", max(test_combination_part_1(p) for p in permutations([4,3,2,1,0])))

print("part2: ", max(test_combination(p) for p in permutations([5,6,7,8,9])))