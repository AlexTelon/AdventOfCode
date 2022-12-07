from collections import defaultdict
from typing import Dict, Iterable

def create_subdir():
    """Ensures that there is always a deeper dict when asked for."""
    return defaultdict(create_subdir)

class Computer():
    root = defaultdict(create_subdir)
    cwd = root
    sizes = {}

    def __init__(self, lines: Iterable[str]):
        for line in lines:
            match line.split():
                case ['$', 'ls']:
                    pass
                case ['$', 'cd', arg]:
                    self.CD(arg)
                case ['dir', name]:
                    pass
                case [size, name]:
                    size = int(size)
                    self.cwd[name] = size

    def CD(self, path):
        if path == '/':
            self.cwd = self.root
        elif path == '..':
            self.cwd = self.cwd['..']
        else:
            # Create way to get back, like real filesystem.
            self.cwd[path]['..'] = self.cwd
            self.cwd = self.cwd[path]


    def calc_size(self, node: Dict, pwd: str = '/'):
        t = 0
        for name, files in node.items():
            if name == '..':
                continue
            if isinstance(files, dict):
                t += self.calc_size(files, pwd + f'{name}/')
            else:
                size = files 
                t += size
        self.sizes[pwd] = t
        return t

if __name__ == '__main__':

    with open('input.txt', 'r') as f:
        lines = f.read().splitlines()

    computer = Computer(lines)
    used_size = computer.calc_size(computer.root)

    print('p1', sum(size for size in computer.sizes.values() if size <= 100_000))

    allowed = 70_000_000
    candidates = [path for path, size in computer.sizes.items() if allowed-(used_size-size) >= 30000000]
    ans = sorted(candidates, key=lambda x: computer.sizes[x])[0]
    print('p2', computer.sizes[ans], f'(path: {ans})')