from collections import defaultdict

lines = open('input.txt').read().splitlines()

p1 = 0
for line in lines:
    left, digits = line.split('|')

    lens = [len(word) for word in digits.split()]
    p1 += len([l for l in lens if l in [2, 3, 4, 7]])
print('p1', p1)

p2 = 0
for line in lines:
    # left side is 10 scrambled unique patterns. one for each digit.
    # Right side is the four digits we are after.
    scrambled, four_digits = line.split('|')

    # Below we use a lot of set logic to get be able to say things like
    # letter_c = letters_cb - letter_b
    ALL = set('a b c d e f g'.split())

    # How long each 'word' is. Where word contains the scrambled segments for a digit.
    lengths = defaultdict(list)
    for word in scrambled.split():
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
        n = scrambled.count(letter)
        if n == 4:
            letter_e = set(letter)
        elif n == 9:
            letter_f = set(letter)
        elif n == 6:
            letter_b = set(letter)

    # Some letters have a uniqe number of segments. (p1 basically)
    # count: numbers with that count
    #     2: [1],
    #     3: [7],
    #     4: [4],
    #     5: [2, 3, 5],
    #     6: [0, 6, 9],
    #     7: [8],
    one = lengths[2][0]
    seven = lengths[3][0]
    eight = lengths[7][0]
    four = lengths[4][0]
    del lengths[2]
    del lengths[3]
    del lengths[7]
    del lengths[4]

    letter_a = seven - one
    letters_cf = one
    letter_c = letters_cf - letter_f

    # we have letters
    # a, b, c, _, e, f, _
    # we have digits
    # _, 1, _, _, 4, _, _, 7, 8, _

    for word in lengths[5]:
        # only 3, 5, 6 included.
        # 5 and 6 both have only f.
        # 3 has both.
        if len(word.intersection(letters_cf)) == 2:
            three = word
    lengths[5].remove(three)
    
    # we have letters
    # a, b, c, _, e, f, _
    # we have digits
    # _, 1, _, 3, 4, _, _, 7, 8, _
    # lengths left
    # 5: [2, 5],
    # 6: [0, 6, 9],

    # letter_b is only in five, not in two.
    for word in lengths[5]:
        if any(word.intersection(letter_b)):
            five = word
        else:
            two = word
    # no more length 5 digits left
    del lengths[5]

    # we now have length 6 items only
    # [0, 6, 9]
    # 9 is the only one without letter_e
    for word in lengths[6]:
        if not any(word.intersection(letter_e)):
            nine = word
    lengths[6].remove(nine)

    # 0, 6 left
    # 6 does not have letter_c
    for word in lengths[6]:
        if not any(word.intersection(letter_c)):
            six = word
        else:
            zero = word
    del lengths[6]
    
    # We now have a reference for all digits.
    DIGITS = [zero, one, two, three, four, five, six, seven, eight, nine]
    
    # tansform to sets and see which digits each coresponds to.
    four_digits = [set(word) for word in four_digits.split()]

    p2 += int(''.join(str(DIGITS.index(d)) for d in four_digits))
print('p2', p2)