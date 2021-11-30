import string

passports = []
passport = {}
lines = iter(open('input.txt').read().splitlines() + [''])
for line in lines:
    while line.strip() != "":
        for item in line.split():
            key, value = item.split(':')
            passport[key] = value
        # passport.update({}.fromkeys([tuple(item.split(':')) for item in line.split()]))
        line = next(lines)
    passports.append(passport)
    passport = {}

def validate_passport(passport: dict):
    must_haves = ['byr','iyr','eyr','hgt','hcl','ecl','pid']
    
    if not all(key in passport for key in must_haves):
        return False
    # return True
    rules = []
    try:
        rules.append(lambda passport: int(passport['byr']) in range(1920,2002+1))
        rules.append(lambda passport: int(passport['iyr']) in range(2010,2020+1))
        rules.append(lambda passport: int(passport['eyr']) in range(2020,2030+1))

        def height(passport):
            hgt = passport['hgt']
            num = int(hgt[:-2])
            if hgt.endswith('cm'):
                return num in range(150,193+1)
            if hgt.endswith('in'):
                return num in range(59,76+1)
            return False
        rules.append(height)
        
        def hair_colour(passport):
            hcl = passport['hcl']
            if hcl[0] != '#':
                return False
            hcl = hcl[1:]
            
            valid_letters = '0123456789'+string.ascii_lowercase
            return all(c in valid_letters for c in hcl)
        
        rules.append(hair_colour)

        rules.append(lambda passport: passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'])

        rules.append(lambda passport: all(c in '0123456789' for c in passport['pid']) and len(passport['pid']) == 9)

        # print(list(rule(passport) for rule in rules))
        return all(rule(passport) for rule in rules)

    except:
        return False



print('p1',sum(validate_passport(passport) for passport in passports))
# part1 09:24

# part2 20:22