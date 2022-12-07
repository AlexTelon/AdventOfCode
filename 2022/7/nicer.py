from collections import defaultdict
from typing import Dict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def create_subdir():
    """Ensures that there is always a deeper dict when asked for."""
    return defaultdict(create_subdir)

root = defaultdict(create_subdir)
directory = root
for line in lines:
    match line.split():
        case ['$', 'ls']:
            ...
        case ['$', 'cd', '/']:
            directory = root
        case ['$', 'cd', '..']:
            directory = directory['..']
        case ['$', 'cd', arg]:
            # Create way to get back, like real filesystem.
            directory[arg]['..'] = directory
            # Move.
            directory = directory[arg]
        case ['dir', name]:
            ...
        case [size, name]:
            size = int(size)
            directory[name] = size

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

used_size = calc_size(root, '/')

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

ans = sorted(candidates, key=lambda x: sizes[x])[0]

print('p2', sizes[ans], f'(path: {ans}, space left, {space_left})')