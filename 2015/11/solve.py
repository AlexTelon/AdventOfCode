import string

def index(letter):
    return string.ascii_lowercase.index(letter)

def next_letter(letter):
    i = index(letter)
    n = len(string.ascii_lowercase)
    if (i + 1) == n:
        return 1, string.ascii_lowercase[0]
    else:
        return 0, string.ascii_lowercase[(i + 1)]
    # return string.ascii_lowercase[(i + 1) % n]

def next_password(password):
    overflow = 1
    result = ""
    for c in reversed(password):
        if overflow:
            overflow, c = next_letter(c)
        result += c
    
    return ''.join(reversed(result))

def next_valid_password(password):
    password = next_password(password)
    # print(password)
    while not valid_password(password):
        password = next_password(password)
        # print(password)
        # if password.startswith('abcdfezz'):
        #     print('hi')
    return password


def valid_password(password):
    if any(letter in password for letter in 'iol'):
        return False
    
    # two non-overlaping pairs.
    pairs = set()
    for a,b in zip(password, password[1:]):
        if a == b:
            pairs.add(a)
    if len(pairs) < 2:
        return False

    # Three consecutive letters.
    for a,b,c in zip(password, password[1:], password[2:]):
        if index(a)+2 == index(b)+1 == index(c):
            return True
    return False

assert not valid_password('hijklmmn')
assert not valid_password('abbceffg')
assert not valid_password('abbcegjk')
assert valid_password('abcdffaa')

assert next_valid_password('abcdefgh') == 'abcdffaa'
# assert next_valid_password('ghijklmn') == 'ghjaabcc'

print('p1', next_valid_password('hxbxwxba'))
print('p2', next_valid_password('hxbxxyzz'))
# part 2: 19:00