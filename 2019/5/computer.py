from collections import namedtuple
import collections
import itertools
import functools

DebugInfo = namedtuple('DebugInfo', ['pc', 'name', 'args',])


def instruction(nr_of_args):
    def real_decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            self = args[0]
            instruction_args = self.fetch_and_step(nr_of_args)

            info = DebugInfo(name=function.__name__,
                pc=self.pc,
                args=instruction_args
            )
            self.debug_info.append(info)
            if self.debug:
                print(f"{self.pc}{function.__name__: >10} {instruction_args}\t\t unpacked args: {[self.data[x] for x in instruction_args]}", end="")

            # execute
            # try:
            result = function(self, *instruction_args)
            # except IndexError as e:
            #     print()
            #     print(f"args causing the index error: {instruction_args}")
            #     print()
            #     raise e

            if self.debug:
                pass
                print(f"\t\t data at last arg position afterwards: {self.data[instruction_args[-1]]}", end="")
                print(f"data[0]: {self.data[0]}")
            return result
        return wrapper
    return real_decorator


class Computer():

    def load_memory(self, file):
        self.data = []
        with open(file, 'r') as f:
            self.data = list(map(int, f.read().split(',')))

    def fetch_and_step(self, nr):
        """Fetches a slice of memory and increments pc."""
        i = self.pc
        self.pc += nr
        return self.data[i:i+nr]

    @instruction(3)
    def add(self, *args):
        stuff = []
        # for i, x in enumerate(self.param_mode[::-1]):
        modes = []
        for i in range(3):
            x = 0
            if len(self.param_mode) > i:
                x = self.param_mode[::-1][i]
            modes.append(x)

            if x == 0:
                stuff.append(args[i])
            elif x == 1:
                stuff.append(args[i])

        a,b,c = stuff

        if modes[0] == 0:
            a = self.data[a]
        if modes[1] == 0:
            b = self.data[b]

        self.data[c] = a + b

    @instruction(3)
    def minus(self, a, b, c):
        self.data[c] = (self.data[a] - self.data[b])

        # # for i, x in enumerate(self.param_mode[::-1]):
        # for i in range(3):
        #     x = 0
        #     if len(self.param_mode) > i:
        #         x = self.param_mode[::-1][i]

        #     if x == 0:
        #         val = args[i]
        #         stuff.append(self.data[val])
        #     elif x == 1:
        #         stuff.append(args[i])

    @instruction(3)
    def multiply(self, *args):
        stuff = []
        # for i, x in enumerate(self.param_mode[::-1]):
        modes = []
        for i in range(3):
            x = 0
            if len(self.param_mode) > i:
                x = self.param_mode[::-1][i]
            modes.append(x)

            if x == 0:
                stuff.append(args[i])
            elif x == 1:
                stuff.append(args[i])
                # val = args[i]
                # stuff.append(self.data[val])

        # a, b, c = stuff
        # pair = list(zip(stuff, modes))
        # arguments = []
        # for x, mode in zip(stuff, modes):
        #     if mode == 0:
        #         arguments.append(self.data[x])
        #     else:
        #         arguments.append(x)
        
        # a, b, c = [x if mode == 0 else self.data[x] for x, mode in zip(stuff, modes)]
        a,b,c = stuff

        if modes[0] == 0:
            a = self.data[a]
        if modes[1] == 0:
            b = self.data[b]

        self.data[c] = a * b

    # @instruction(3)
    # def divide(self, a, b, c):
    #     self.data[c] = (self.data[a] // self.data[b])

    def halt(self):
        self.abort = True

    @instruction(1)
    def input(self, addr):
        self.data[addr] = int(input())
    
    @instruction(1)
    def output(self, a):
        mode = self.param_mode[0]
        if mode == 0:
            a = self.data[a]
        print(a)



    @instruction(2)
    def jmp_true(self, expr, jmp_addr):
        modes = []
        for i in range(3):
            x = 0
            if len(self.param_mode) > i:
                x = self.param_mode[::-1][i]
            modes.append(x)
        if modes[0] == 0:
            expr = self.data[expr]
        if modes[1] == 0:
            jmp_addr = self.data[jmp_addr]

        if expr != 0:
            self.pc = jmp_addr

    @instruction(2)
    def jmp_false(self, expr, jmp_addr):
        modes = []
        for i in range(3):
            x = 0
            if len(self.param_mode) > i:
                x = self.param_mode[::-1][i]
            modes.append(x)
        if modes[0] == 0:
            expr = self.data[expr]
        if modes[1] == 0:
            jmp_addr = self.data[jmp_addr]

        if expr == 0:
            self.pc = jmp_addr

    @instruction(3)
    def less_than(self, a, b, addr):
        modes = []
        for i in range(3):
            x = 0
            if len(self.param_mode) > i:
                x = self.param_mode[::-1][i]
            modes.append(x)

        if modes[0] == 0:
            a = self.data[a]
        if modes[1] == 0:
            b = self.data[b]

        result = 0
        if a < b:
            result = 1
        self.data[addr] = result


    @instruction(3)
    def equals(self, a, b, addr):
        modes = []
        for i in range(3):
            x = 0
            if len(self.param_mode) > i:
                x = self.param_mode[::-1][i]
            modes.append(x)

        if modes[0] == 0:
            a = self.data[a]
        if modes[1] == 0:
            b = self.data[b]


        result = 0
        if a == b:
            result = 1
        self.data[addr] = result
 
    # @instruction(3)
    # def jmp_eq(self, jmp, a, b):
    #     """Jump if equal"""
    #     if a == b:
    #         self.pc = jmp_addr

    # @instruction(3)
    # def jmp_neq(self, jmp, a, b):
    #     """Jump if not equal"""
    #     if a != b:
    #         self.pc = jmp_addr

    # @instruction(3)
    # def jmp_neq(self, jmp, a, b):
    #     """Jump if not equal"""
    #     if a != b:
    #         self.pc = jmp_addr

    # @instruction(1)
    # def pop(self, a):
    #     self.data[a] = self.stack.popleft()

    # @instruction(1)
    # def push(self, a):
    #     self.stack.pushleft(self.data[a])


    # @property
    # def pc(self):
    #     return self.__pc

    # @pc.setter
    # def pc(self, value):
    #     self.__pc = value


    def __init__(self, debug=False):
        self.pc = 0
        self.abort = False
        self.debug = debug

        self.debug_info = []

        # 3: self.minus,
        # 4: self.divide,
        # 21: self.jmp,
        self.op_codes = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jmp_true,
            6: self.jmp_false,
            7: self.less_than,
            8: self.equals,
            99: self.halt,
        }

    def _exec_instruction(self, op):
        # if self.debug:
        #     print(f"{self.op_codes[op].__name__}")
        instruction = self.op_codes[op]
        instruction()

    def tick(self):
        # op, = self.fetch_and_step(1)
        # op, = self.fetch_and_step(1)
        op, = self.data[self.pc:self.pc+1]
        self.pc += 1

        nums = [int(i) for i in str(op)]
        self.param_mode = [0,0]
        if len(nums) <= 2:
            # normal stuff
            pass
        else:
            op = nums[-2:]
            op = int(op[1]) # hack for now, change halt to 99 again afterwards
            if op == 9:
                op == 99
            self.param_mode = nums[:-2]
        
        self._exec_instruction(op)

    def run(self):
        self.pc = 0
        self.abort = False
        while not self.abort:
            self.tick()

# 3,12 - write to addr 12
# 6,12,15,1 - jump to 1 addr[6] == addr[15]
# ,13,14,13,4,13,99,-1,0,1,9

# somethign is wrong with the last 9

# 225 is too low

if __name__ == "__main__":

    computer = Computer(debug=False)

    computer.load_memory('input.txt')

    # computer.data = list(map(int, f.read().split(',')))

    # print("-----------")
    # print(computer.data)

    computer.run()

    # print("-----------")
    # print(computer.data)

# TODO add a way to show where PC is relative to data
# TODO add a way to convert all OP_codes in data to named functions and then split after the right nr of args