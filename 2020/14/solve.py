from collections import defaultdict
from itertools import zip_longest

lines = open(0).read().splitlines()
# lines = open('input.txt').read().splitlines()
lines = [line.split() for line in lines]

def to_bits(num):
    return f"{int(num):036b}"

# part 1
def bitmask_num(mask, num):
    result = ""
    for m, c in zip_longest(mask, to_bits(num)):
        if m == "X":
            result += c
        else:
            result += m
    print(result, "->", int(result, 2))
    return int(result, 2)

# part 2
def addresses(mask, adr):
    pattern = ""
    for m, c in zip_longest(mask, to_bits(adr)):
        if m == '0':
            pattern += c
        if m == '1':
            pattern += '1'
        if m == "X":
            pattern += 'X'
    
    results = [""]
    for c in pattern:
        if c == 'X':
            for i in range(len(results)):
                # Duplicate.
                new = results[i] + "1"
                results.append(new)

                # Extend existing.
                results[i] = results[i] + '0'
        else:
            # Just extend.
            for i in range(len(results)):
                results[i] += c
    return [int(x, 2) for x in results]


mem = defaultdict(int)
mask = ""
for line in lines:
    if line[0] == 'mask':
        mask = line[2]
    else:
        adr, _, num = line
        adr = int(adr.replace("mem[", "").replace("]", ""))
        # part 1
        # mem[adr] = int(bitmask_num(mask, num))
        # part 2
        num = int(num)
        for adr in addresses(mask, adr):
            mem[adr] = num

print("result", sum(x for x in mem.values()))