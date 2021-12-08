from collections import defaultdict

lines = open('input.txt').read().splitlines()

p1 = 0
for line in lines:
    left, digits = line.split('|')

    lens = [len(d) for d in digits.split()]
    p1 += len([l for l in lens if l in [2, 3, 4, 7]])
print('p1', p1)

p2 = 0
for line in lines:
    reference_10, four_digits = line.split('|')

    # How long each 'word' is. Where word contains the scrambled segments for a digit.
    lengths = defaultdict(list)
    for word in reference_10.split():
        lengths[len(word)].append(set(word))

    # Counting all letters for all 10 unique patterns and we find that
    # 3 of them have a unique count. Those letters we can assign right away.
    # Below is which letters occur how many times. 
    #    8: ['a', 'c'],
    #    6: ['b'],
    #    7: ['d', 'g'],
    #    4: ['e'],
    #    9: ['f'],
    for letter in 'abcdefg':
        n = reference_10.count(letter)
        if n == 4: _e = set(letter)
        elif n == 9: _f = set(letter)
        elif n == 6: _b = set(letter)

    # A few unique length words.
    _1 = lengths[2][0]
    _7 = lengths[3][0]
    _8 = lengths[7][0]
    _4 = lengths[4][0]

    _cf = _1
    _c = _cf - _f

    # nifty thing in python. Easy to create an alias to a function like this
    first = next

    _3 = first(w for w in lengths[5] if len(w.intersection(_cf)) == 2)
    lengths[5].remove(_3)
    _5 = first(w for w in lengths[5] if any(w.intersection(_b)))
    _2 = first(w for w in lengths[5] if not any(w.intersection(_b)))

    _9 = first(w for w in lengths[6] if not any(w.intersection(_e)))
    lengths[6].remove(_9)
    _6 = first(w for w in lengths[6] if not any(w.intersection(_c)))
    _0 = first(w for w in lengths[6] if any(w.intersection(_c)))
    
    # We now have a reference for all digits.
    DIGITS = [_0, _1, _2, _3, _4, _5, _6, _7, _8, _9]
    
    # tansform to sets and see which digits each corresponds to.
    four_digits = [set(d) for d in four_digits.split()]

    p2 += int(''.join(str(DIGITS.index(d)) for d in four_digits))
print('p2', p2)