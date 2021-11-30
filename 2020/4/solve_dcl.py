import inspect
import string
import sys
import re
from functools import wraps

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


# All validator functions are saved here by the use of the validator below.
validators = set()

def validator(f):
    @wraps(f)
    def wrapper(*args):
        passport = args[0]
        value = passport[f.__name__]
        return f(value)
    validators.add(wrapper)
    return wrapper

# Functions. The name of each function determines which value it checks.

@validator
def byr(value):
    return 1920 <= int(value) <= 2002

@validator
def iyr(value):
    return 2010 <= int(value) <= 2020

@validator
def eyr(value):
    return 2020 <= int(value) <= 2030

@validator
def ecl(value):
    return value in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

@validator
def pid(value):
    return all(c in '0123456789' for c in value) and len(value) == 9

@validator
def hgt(value):
    num = int(value[:-2])
    if value.endswith('cm'):
        return 150 <= num <= 193
    if value.endswith('in'):
        return 59 <= num <= 76
    return False

@validator
def hcl(value):
    if value[0] != '#':
        return False
    value = value[1:]
    
    valid_letters = '0123456789'+string.ascii_lowercase
    return all(c in valid_letters for c in value)


def is_valid(passport):
    try:
        return all(validator(passport) for validator in validators)
    except Exception as e:
        return False


if __name__ == "__main__":
    print(sum(is_valid(passport) for passport in passports))
    print('len', len(passports))