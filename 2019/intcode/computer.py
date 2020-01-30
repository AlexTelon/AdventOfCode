from collections import namedtuple
from collections import defaultdict
from inspect import signature

import collections
import itertools
import functools

# Needs pip install
from defaultlist import defaultlist

DebugInfo = namedtuple('DebugInfo', ['pc', 'name', 'args',])

def instruction():
    def real_decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):

            sig = signature(function)
            # The number of parameters minus "self"
            nr_of_args = len(sig.parameters) - 1

            self = args[0]
            instruction_args = self.fetch_and_step(nr_of_args)

            # Gather some debug information
            info = DebugInfo(name=function.__name__,
                pc=self.pc,
                args=instruction_args
            )
            self.debug_info.append(info)

            result = function(self, *instruction_args)
            return result
        return wrapper
    return real_decorator


class Computer():

    def load_memory(self, file):
        self.data = defaultlist(int)
        with open(file, 'r') as f:
            for x in map(int, f.read().split(',')):
                self.data.append(x)

    def fetch_and_step(self, nr):
        """Fetches a slice of memory and increments pc."""
        i = self.pc
        self.pc += nr

        # Arguments according to parameter mode
        self.args = []
        # The raw arguments. Needed for write parameters.
        self.args_raw = self.data[i:i+nr]

        for i, arg in enumerate(self.args_raw):
            mode = self.param_mode[i]
            if mode == 0:
                self.args.append(self.data[arg])
            elif mode == 1:
                self.args.append(arg)
            else:
                pos = self.relative_base + arg
                self.args.append(self.data[pos])

        return self.args

    def get_addr(self, index):
        """Used by instructions to get their write addr. It handles param modes for you.
        
        Why is it not a normal parameter? Because normally in non-immediate mode the contents of the memory addr is used.
        But when writing we only want the address which this function can provide.
        """
        # Day5: "Parameters that an instruction writes to will never be in immediate mode."
        param_mode = self.param_mode[index]
        if param_mode == 2:
            return self.args_raw[index] + self.relative_base
        else:
            return self.args_raw[index]

    @instruction()
    def add(self, a, b, addr):
        addr = self.get_addr(2)
        self.data[addr] = a + b

    @instruction()
    def multiply(self, a, b, _):
        addr = self.get_addr(2)
        self.data[addr] = a * b

    def halt(self):
        self.abort = True

    @instruction()
    def input(self, _):
        addr = self.get_addr(0)
        item = int(input())
        # item = self.input_queue.get()

        self.data[addr] = item

    @instruction()
    def output(self, a):
        print(f"output: {a}")
        self.output_stuff = a
        # self.output_queue.put(a)

    @instruction()
    def jmp_true(self, expr, jmp_addr):
        if expr != 0:
            self.pc = jmp_addr

    @instruction()
    def jmp_false(self, expr, jmp_addr):
        if expr == 0:
            self.pc = jmp_addr

    @instruction()
    def less_than(self, a, b, _):
        addr = self.get_addr(2)
        result = 0
        if a < b:
            result = 1
        self.data[addr] = result


    @instruction()
    def equals(self, a, b, _):
        addr = self.get_addr(2)
        result = 0
        if a == b:
            result = 1
        self.data[addr] = result

    @instruction()
    def relative(self, shift):
        self.relative_base += shift


    def __init__(self):
        self.pc = 0
        self.abort = False

        self.debug_info = []

        self.relative_base = 0

        self.op_codes = {
            1: self.add,
            2: self.multiply,
            3: self.input,
            4: self.output,
            5: self.jmp_true,
            6: self.jmp_false,
            7: self.less_than,
            8: self.equals,
            9: self.relative,
            99: self.halt,
        }

    def _exec_instruction(self, op):
        instruction = self.op_codes[op]
        instruction()

    def tick(self):
        op, = self.data[self.pc:self.pc+1]
        self.pc += 1

        nums = [int(i) for i in str(op)]

        self.param_mode = defaultdict(int)


        if len(nums) <= 2:
            # normal stuff
            pass
        else:
            op = nums[-2:]
            op = int(op[1]) # hack for now, change halt to 99 again afterwards
            if op == 9:
                op == 99
            nums = list(reversed(nums[:-2]))
            for i, x in enumerate(nums):
                self.param_mode[i] = x

        self._exec_instruction(op)

    def run(self):
        self.pc = 0
        self.abort = False
        while not self.abort:
            self.tick()


if __name__ == "__main__":

    computer = Computer()
    computer.load_memory('input.txt')
    computer.run()