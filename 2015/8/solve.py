n_chars = 0
mem_chars = 0
for line in open('input.txt').read().splitlines():
    n_chars += len(line)

    it = iter(line[1:-1])
    local = 0
    for c in it:
        if c == '\\':
            a = next(it)
            if a == 'x':
                # \xFF case
                next(it)
                next(it)
            else:
                # \\ case
                # \" case
                pass

        local += 1
    mem_chars += local

print('p1:', n_chars - mem_chars)
# part 1 10:49

p2_len = 0
for line in open('input.txt').read().splitlines():
    line = line.replace('\\', '\\\\')
    line = line.replace('"', '\\"')
    line = '"' + line + '"'
    p2_len += len(line)

print(p2_len - n_chars)
# part 2 14:28