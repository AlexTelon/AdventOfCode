import collections
import itertools

def add(a, b, c):
    global data
    data[c] = (data[a] + data[b])

def multiply(a, b, c):
    global data
    data[c] = (data[a] * data[b])

# def halt(*args):
#     exit()

op_codes = {
    1: add,
    2: multiply,
    99: halt,
}

def load_memory(file):
    global data
    data = []
    with open(file, 'r') as f:
        data = list(map(int, f.read().split(',')))

def run_program():
    pc = 0
    while True:
        op = data[pc]
        args = data[pc+1:pc+4]
        if op == 99:
            break
        op_codes[op](*args)
        pc += 4


if __name__ == "__main__":
    for noun in range(100):
        for verb in range(100):
            
            load_memory('input.txt')
            data[1] = noun
            data[2] = verb

            print(f'{noun} {verb}')
            run_program()

            if data[0] == 19690720:
                print(data[0])
                print(f"Answer: 100 * {noun} + {verb} == {100 * noun + verb}")
                exit()