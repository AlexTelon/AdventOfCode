lines = open('input.txt').read().splitlines()
lines = [[x for x in line.split()] for line in lines]

count_1 = 0
count_2 = 0

for policy, letter, password in lines:
    low, high = map(int, policy.split('-'))
    letter = letter[:-1]

    if low <= password.count(letter) <= high:
        count_1 += 1

    new = password[low-1] + password[high-1]
    if new.count(letter) == 1:
        count_2 += 1

print(f"part1: {count_1}")
print(f"part2: {count_2}")