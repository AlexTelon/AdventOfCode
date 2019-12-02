import collections
import itertools
import functools

def instruction(nr_of_args):
    def real_decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            self = args[0]
            if self.debug:
                print(f"instruction args:{args} nr_of_args: {nr_of_args}")
            result = function(self, *self.fetch_and_step(nr_of_args))
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
    def multiply(self, a, b, c):
        self.data[c] = (self.data[a] * self.data[b])

    def halt(self):
        self.abort = True

    # def jmp(self):
    #     jmp_addr = self.fetch_and_step(1)
    #     self.pc = jmp_addr

    # def jmp_eq(self):
    #     """Jump if equal"""
    #     jmp, a, b = self.fetch_and_step(3)
    #     if a == b:
    #         self.pc = jmp_addr

    # def jmp_neq(self):
    #     """Jump if not equal"""
    #     jmp, a, b = self.fetch_and_step(3)
    #     if a != b:
    #         self.pc = jmp_addr


    @property
    def pc(self):
        return self.__pc

    @pc.setter
    def pc(self, value):
        self.__pc = value


    def __init__(self, debug=False):
        self.pc = 0
        self.abort = False
        self.debug = debug
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

    computer = Computer(debug=True)

    computer.load_memory('input.txt')
    computer.run()