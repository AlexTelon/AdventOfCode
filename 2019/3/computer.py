import collections
import itertools
import functools

def instruction(nr_of_args):
    def real_decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            self = args[0]
            instruction_args = self.fetch_and_step(nr_of_args)

            if self.debug:
                print(f"{function.__name__: >10} {instruction_args}\t\t unpacked args: {[self.data[x] for x in instruction_args]}", end="")

            # execute
            result = function(self, *instruction_args)
            if self.debug:
                print(f"\t\t data at last arg position afterwards: {self.data[instruction_args[-1]]}", end="")
                print(f"\tpc: {self.pc}")
                # print(f"data[0]: {self.data[0]}")
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
    def add(self, a, b, c):
        self.data[c] = (self.data[a] + self.data[b])

    @instruction(3)
    def minus(self, a, b, c):
        self.data[c] = (self.data[a] - self.data[b])

    @instruction(3)
    def multiply(self, a, b, c):
        self.data[c] = (self.data[a] * self.data[b])

    @instruction(3)
    def divide(self, a, b, c):
        self.data[c] = (self.data[a] // self.data[b])

    def halt(self):
        self.abort = True

    # @instruction(1)
    # def jmp(self, jmp_addr):
    #     self.pc = jmp_addr

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

    @instruction(1)
    def pop(self, a):
        self.data[a] = self.stack.popleft()

    @instruction(1)
    def push(self, a):
        self.stack.pushleft(self.data[a])


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
        # 3: self.minus,
        # 4: self.divide,
        # 10: self.jmp_eq,
        # 21: self.jmp,
        self.op_codes = {
            1: self.add,
            2: self.multiply,
            99: self.halt,
        }

    def _exec_instruction(self, op):
        # if self.debug:
        #     print(f"{self.op_codes[op].__name__}")
        instruction = self.op_codes[op]
        instruction()

    def run(self):
        self.pc = 0
        self.abort = False
        while not self.abort:
            op, = self.fetch_and_step(1)
            self._exec_instruction(op)


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