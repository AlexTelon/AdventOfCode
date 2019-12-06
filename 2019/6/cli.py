# A cli interface for the computer
# To begin with I want a good debug interface where I can step through the code

import computer
import argparse
import itertools

def print_data(computer, before=None, after=None):
    start = 0
    end = -1
    if before is not None:
        start = max(computer.pc - before, 0)
    if after is not None:
        end = min(computer.pc + after, len(computer.data))

    for i, x in enumerate(computer.data[start:end], start=computer.pc):
        if i == computer.pc:
            print(f"_{x}_", end=", ")
        else:
            print(x, end=", ")
    print()

def print_debug_info(debug_info):
    print(debug_info.name, debug_info.args)
    # for prop in debug_info:
    #     print(prop, end=", ")
    # print()


parser = argparse.ArgumentParser()
parser.add_argument("--debug", help="debug mode", action="store_true")
parser.add_argument("-i", "--interactive", help="debug mode", action="store_true")
args = parser.parse_args()

# if args.interactive:
#     args.debug = True

computer = computer.Computer(debug=args.debug)
computer.load_memory('input.txt')
# computer.run()

if args.interactive:
    previous_input = ''
    # print("i,op\tpc arg refs,\t\t arg as value \t ")
    extra_info = False
    follow = []
    print("==============================================================================================================")
    for i in itertools.count():
        # print(i, end=" ")
        
        while True:
            current_input = input(">")
            # Enter should re-run the previous one
            if current_input in ['']:
                current_input = previous_input

            if current_input in ['q', 'quit', 'exit']:
                exit()
            elif current_input in ['s', 'step', 'n', 'next']:
                break
            elif current_input in ['+']:
                extra_info = True
            elif current_input in ['-']:
                extra_info = False
            elif current_input[:6] == 'follow':
                follow = list(map(int, current_input[6:].split()))
                print(follow)

            elif current_input in ['?']:
                print("step:\t[s, step, n, next]")
                print("quit:\t[q, quit, exit]")
                print("?:\t[?] - show this menu")


        print_debug_info(computer.debug_info[-1])
        if extra_info:
            print_data(computer, before=0, after=10)
        if any(follow):
            print("data:")
            print("\n".join(f"index:{x}, val:{computer.data[x]}" for x in follow))

        computer.tick()
        previous_input = current_input