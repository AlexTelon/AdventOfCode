import itertools

data = [line for line in open('input.txt')]

vowels = 'aeiou'
alphabet = 'abcdefghijklmnopqrstuvwxyz'

def is_nice(line):
    if any(x in line for x in ["ab", "cd", "pq", "xy"]):
        return False

    if sum(x in vowels for x in line) > 2:
        if any(len(list(g)) > 1 for k, g in itertools.groupby(line)):
            return True

    return False

print(sum(is_nice(line) for line in data))