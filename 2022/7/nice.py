from collections import defaultdict
from typing import Dict

with open('input.txt', 'r') as f:
    lines = f.read().splitlines()

def create_subdir():
    """Ensures that there is always a deeper dict when asked for."""
    return defaultdict(create_subdir)

root = defaultdict(create_subdir)
directory = None
last_command = None
for line in lines:
    command = line.startswith('$')

    if command:
        last_command, *args = line.replace('$ ','').split() + ['']
        if last_command == 'ls':
            # What happens next is a bunch of lines of files and directories.
            # These are parsed in the case when we are not a command further down. 
            ...
        elif last_command == 'cd':
            arg = args[0]
            if arg == '/':
                directory = root
            elif arg == '..':
                directory = directory['..']
            else:
                # Create way to get back, like real filesystem.
                directory[arg]['..'] = directory
                # Move.
                directory = directory[arg]
        else:
            raise Exception('Unknown command!')
    else:
        # The output from ls is parsed here.
        assert last_command == 'ls'
        kind, file = line.split()
        if kind == 'dir':
            continue
        else:
            size = int(kind)
            directory[file] = size

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