import collections
import itertools


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


    def add(self):
        a, b, c = self.fetch_and_step(3)
        self.data[c] = (self.data[a] + self.data[b])

    def multiply(self):
        a, b, c = self.fetch_and_step(3)
        self.data[c] = (self.data[a] * self.data[b])

    def halt(self):
        self.abort = True


    def __init__(self):
        self.abort = False
        self.op_codes = {
            1: self.add,
            2: self.multiply,
            99: self.halt,
        }

    def _exec_instruction(self, op):
        self.op_codes[op]()


    def run(self):
        self.pc = 0
        self.abort = False
        while not self.abort:
            op, = self.fetch_and_step(1)
            self._exec_instruction(op)


if __name__ == "__main__":

    computer = Computer()
    computer.load_memory('input.txt')
    computer.run()