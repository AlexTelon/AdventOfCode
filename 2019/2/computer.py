import collections
import itertools


class Computer():

    def add(self, a, b, c):
        self.data[c] = (self.data[a] + self.data[b])

    def multiply(self, a, b, c):
        self.data[c] = (self.data[a] * self.data[b])

    def halt(self):
        pass

    def __init__(self):
        self.op_codes = {
            1: lambda data: self.add(*data[:3]),
            2: lambda data: self.multiply(*data[:3]),
            99: self.halt,
        }
        
    def load_memory(self, file):
        self.data = []
        with open(file, 'r') as f:
            self.data = list(map(int, f.read().split(',')))

    def run(self):
        self.pc = 0
        while True:
            op = self.data[self.pc]
            # args = data[pc+1:pc+4]
            if op == 99:
                break
            self.op_codes[op](self.data[self.pc+1:])
            self.pc += 4


if __name__ == "__main__":

    computer = Computer()
    computer.load_memory('input.txt')
    computer.run()