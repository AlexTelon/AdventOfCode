from collections import defaultdict
from typing import Dict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

directory = defaultdict(dict)
current_directory = None
last_command = None
for line in lines:
    command = line.startswith('$')

    if command:
        _, *op = line.split()
        if op[0] == 'ls':
            last_command = 'ls'
        elif op[0] == 'cd':
            last_command = 'cd'
            args = op
            arg = args[-1]
            if arg == '/':
                current_directory = directory
            elif arg == '..':
                current_directory = current_directory['..']
            else:
                # Implicit create.
                current_directory[arg] = {}
                # Create way to get back, like real filesystem.
                current_directory[arg]['..'] = current_directory
                # Move.
                current_directory = current_directory[arg]
        else:
            raise Exception('Unknown command!')
    else:
        assert last_command == 'ls'
        kind, file = line.split()
        if kind == 'dir':
            continue
        else:
            size = int(kind)
            current_directory[file] = size

sizes = {}
def calc_size(node: Dict, pwd: str):
    t = 0
    for name, files in node.items():
        if name == '..':
            continue
        if isinstance(files, dict):
            t += calc_size(files, pwd + f'{name}/')
        else:
            size = files 
            t += size
    sizes[pwd] = t
    return t

used_size = calc_size(directory, '/')

p1 = 0
for path, size in sizes.items():
    if size <= 100_000:
        p1 += size
print('p1', p1)

allowed = 70_000_000
candidates = []
for path, size in sizes.items():
    space_left = allowed-(used_size-sizes[path])
    if space_left >= 30000000:
        candidates.append(path)
ans = sorted(candidates, key= lambda x: sizes[x])[0]

print('p2', sizes[ans], f'(path: {ans}, space left, {space_left})')