from collections import deque
import operator
import math

hex_data = open('input.txt').read()
bin_data = deque([bin(int(i, 16))[2:].zfill(4) for i in hex_data.strip()])

bits = deque()
bits_read = 0
def get_n_bits(n):
    """Helper function that fetches n bits for me. As Im unsure if I might need to always keep track of which 'word' we are at"""
    assert n > 0
    global bits_read
    result = []
    while n:
        if len(bits) == 0:
            # get the next word (hex number (4 bits.))
            bits.extend(bin_data.popleft())

        result.append(bits.popleft())
        n -= 1
        bits_read += 1
    return ''.join(result)

p1 = 0

def parse_packet():
    """Parses a packet. Returns the number of bits parsed and the value of the packet."""
    number = ""
    global p1

    # HEADER. 
    version = get_n_bits(3)
    type_id = get_n_bits(3)

    p1 += int(version, 2)
    type_id = int(type_id,2)

    literal = type_id == 4
    if literal:
        while True:
            match tuple(get_n_bits(5)):
                case '1', a, b, c, d:
                    number += a + b + c + d
                case '0', a, b, c, d:
                    number += a + b + c + d
                    # starting with 0 indicates that we are done!
                    break
        
        return int(number,2)
    else:
        # Operator.
        # One or more packets. Add the subpacket values to a list. Then do an operation on them.
        values = []

        length_type_id = get_n_bits(1)
        if length_type_id == '0':
            total_length_of_subpackets = int(get_n_bits(15), 2)
            goal = bits_read + total_length_of_subpackets
            while bits_read != goal:
                values.append(parse_packet())
        else:
            num_of_subpackets = int(get_n_bits(11), 2)
            for _ in range(num_of_subpackets):
                values.append(parse_packet())

        operators = {
            0: sum,
            1: math.prod,
            2: min,
            3: max,
            5: operator.gt,
            6: operator.lt,
            7: operator.eq,
        }
        op = operators[type_id]
        if type_id in [0, 1, 2, 3]:
            value = op(values)
        else:
            value = op(values[0], values[1])

    return value

def is_only_zeros_left():
    return all(bit == '0' for bit in bits) and all((word == '0000' for word in bin_data))

if __name__ == "__main__":
    while bin_data:
        if is_only_zeros_left():
            break
        value = parse_packet()

    print('p1', p1)
    print('p2', value)