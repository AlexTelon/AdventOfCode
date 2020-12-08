lines = open('input.txt').read().splitlines()
instructions = [line.split() for line in lines]

accumulator = 0
pointer = 0
visited = set()
done = False

def acc(inc):
    global accumulator
    accumulator += inc

def jmp(rel):
    global pointer, done
    pointer += rel
    if pointer == len(instructions):
        print('part2', accumulator)
        exit()
    if pointer not in visited:
        visited.add(pointer)
    else:
        # print(f'will visit {pointer} a second time!')
        # print('part1', accumulator)
        # exit()
        done = True

def nop(num):
    pass

op_codes = {
    'acc' : acc,
    'jmp' : jmp,
    'nop' : nop,
}

def run_computer(instructions):
    while not done:
        op, num = instructions[pointer]
        num = int(num)
        # print(pointer, op, num)
        op_codes[op](num)
        if op != 'jmp':
            op_codes['jmp'](1)

for i, (op, num) in enumerate(instructions):
    # Only swap nop and jmp's.
    if op == "acc":
        continue
    new_op = 'jmp' if op == 'nop' else 'nop'
    print(f'outer loop {i}, {new_op} changed')

    # Change instruction set to one with the changed op-code.
    tmp_instructions = instructions.copy()
    tmp_instructions[i] = (new_op, num)

    # Reset global state
    accumulator = 0
    pointer = 0
    visited = set()
    done = False
    run_computer(tmp_instructions)