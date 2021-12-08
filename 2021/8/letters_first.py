segments_to_digit = {
    'abcefg': '0',
    'cf': '1',
    'acdeg': '2',
    'acdfg': '3',
    'bcdf': '4',
    'abdfg': '5',
    'abdefg': '6',
    'acf': '7',
    'abcdefg': '8',
    'abcdfg': '9',
}

p1 = 0
p2 = 0
for line in open('input.txt').read().splitlines():
    reference_10, four_digits = line.split('|')

    # Each segment is used a fixed number of times for 0 to 9.
    # For instance segment 'e' is only used in 4 digits.
    _ac = set()
    _dg = set()
    for letter in 'abcdefg':
        n = reference_10.count(letter)
        if n == 4:   _e = set(letter)
        elif n == 9: _f = set(letter)
        elif n == 6: _b = set(letter)
        elif n == 7: _dg.add(letter)
        elif n == 8: _ac.add(letter)

    # A few known unique length words.
    _1 = [set(x) for x in reference_10.split() if len(x) == 2][0]
    _4 = [set(x) for x in reference_10.split() if len(x) == 4][0]

    # Deduce the remaining letters.
    _cf = _1
    _c = _cf - _f
    _a = _ac - _c
    _d = _4 - _b - _c - _f
    _g = _dg - _d

    # Mapping between the found letters _a to _g to the actual letters 'a' to 'g'
    table = str.maketrans(''.join(x.pop() for x in [_a, _b, _c, _d, _e, _f, _g]), "abcdefg")
    def translate(letters: str) -> str:
        """Translate the mixed up segment letters to the correct ones."""
        key = ''.join(sorted(letters.translate(table)))
        return segments_to_digit[key]

    digits = [translate(d) for d in four_digits.split()]
    p1 += len([d for d in digits if d in '1478'])
    p2 += int(''.join(digits))
print('p1', p1)
print('p2', p2)