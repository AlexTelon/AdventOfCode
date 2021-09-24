lines = open('input.txt').read().splitlines()

# Input data contains passport data seperated by empty lines.
# First find all passports and then make sure they contain the right type of key:value pairs.
# Then in the second part validiate the values for these mandatory keys.

# Parse the passports.
passports = []
current = {}
for line in lines:
    if line == "":
        passports.append(current)
        current = {}

    for pair in line.split():
        key, value = pair.split(':')
        current[key] = value

# Add the last passport to!
passports.append(current)


def has_required_keys(p):
    required_keys = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    return all(k in p for k in required_keys)


def validate_password(p):
    # Save which keys have been validated and check that all have been validated in the end.
    validated = []

    if 1920 <= int(p['byr']) <= 2002:
        validated.append('byr')
    if 2010 <= int(p['iyr']) <= 2020:
        validated.append('iyr')
    if 2020 <= int(p['eyr']) <= 2030:
        validated.append('eyr')

    if p['hgt'].endswith('cm'):
        if 150 <= int(p['hgt'][:-2]) <= 193:
            validated.append('hgt')
    elif p['hgt'].endswith('in'):
        if 59 <= int(p['hgt'][:-2]) <= 76:
            validated.append('hgt')

    if p['hcl'][0] == '#' and len(p['hcl']) == 7:
        if all('a' <= c <= 'f' or c.isdigit() for c in p['hcl'][1:]):
            validated.append('hcl')

    if p['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        validated.append('ecl')

    if len(str(p['pid'])) == 9 and p['pid'].isdigit():
        validated.append('pid')

    #    print("DEBUG missing ", set(['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']) - set(validated))
    return has_required_keys(validated)
    # return len(validated) == 7


ans_1 = 0
ans_2 = 0
for p in passports:
    # print(p)
    if has_required_keys(p):
        ans_1 += 1

        if validate_password(p):
            ans_2 += 1

print("part1:", ans_1)
print("part2:", ans_2)
# print("all", len(passports))