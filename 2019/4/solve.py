import itertools

def is_ok(num):
    nums = [int(x) for x in str(num)]
    found_eq = False
    for prev, current in zip(nums, nums[1:]):
        if current < prev:
            return False

        # part 1
        # if prev == current:
        #     found_eq = True

        # part 2
        groups = [list(g) for k, g in itertools.groupby(nums)]
        if any(g for g in groups if len(g) == 2):
            found_eq = True

    return found_eq

low, high = 109165, 576723

# part 1
# assert is_ok(111111) is True
# assert is_ok(111123) is True
# assert is_ok(135679) is False
# assert is_ok(223450) is False
# assert is_ok(123789) is False
#part 2
assert is_ok(111123) is False
assert is_ok(111111) is False
assert is_ok(112233) is True
assert is_ok(123444) is False
assert is_ok(111122) is True

#
# unique_passwords = set(password for password in range(low, high+1) if is_ok(password))
print(len([ password for password in range(low, high+1) if is_ok(password) ]))