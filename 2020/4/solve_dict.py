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
    
    def height(passport):
        hgt = passport['hgt']
        if hgt == '97':
            print('hi')
        num = int(hgt[:-2])
        if hgt.endswith('cm'):
            return 150 <= num <= 193
        if hgt.endswith('in'):
            return 59 <= num <= 76
        return False

    def hair_colour(passport):
        hcl = passport['hcl']
        if hcl[0] != '#':
            return False
        hcl = hcl[1:]
        
        valid_letters = '0123456789'+string.ascii_lowercase
        return all(c in valid_letters for c in hcl)

    rules = {
        'byr': lambda passport: 1920 <= int(passport['byr']) <= 2002,
        'iyr': lambda passport: 2010 <= int(passport['iyr']) <= 2020,
        'eyr': lambda passport: 2020 <= int(passport['eyr']) <= 2030,
        'hgt': height,
        'hcl': hair_colour,
        'ecl': lambda passport: passport['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'],
        'pid': lambda passport: all(c in '0123456789' for c in passport['pid']) and len(passport['pid']) == 9,
    }

    try:
        # TODO could add
        return all(rules[rule](passport) for rule in rules)
    except:
        return False



print('p1',sum(validate_passport(passport) for passport in passports))