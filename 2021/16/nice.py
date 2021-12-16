from collections import deque
import operator
from functools import reduce

hex_data = open('input.txt').read()
bits = deque(''.join(bin(int(i, 16))[2:].zfill(4) for i in hex_data.strip()))

global_bits_read = 0
def get_n_bits(n):
    """Helper function that fetches n bits for me."""
    global global_bits_read
    global_bits_read += n
    return ''.join([bits.popleft() for _ in range(n)])

def parse_packet():
    """Parses a packet. Returns the value of the packet."""
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
            last = get_n_bits(1) == '0'
            number += get_n_bits(4)
            if last:
                break

        return int(number,2)
    else:
        # Operator.
        # One or more packets. Add the subpacket values to a list. Then do an operation on them.
        # Each subpacket returns a value. Perform the operator on them.
        values = []

        length_type_id = get_n_bits(1)
        if length_type_id == '0':
            total_length_of_subpackets = int(get_n_bits(15), 2)
            goal = global_bits_read + total_length_of_subpackets
            while global_bits_read != goal:
                values.append(parse_packet())
        else:
            num_of_subpackets = int(get_n_bits(11), 2)
            for _ in range(num_of_subpackets):
                values.append(parse_packet())

        # Apply the correct operator on all values
        operators = {
            0: operator.add,
            1: operator.mul,
            2: min,
            3: max,
            5: operator.gt,
            6: operator.lt,
            7: operator.eq,
        }
        return reduce(operators[type_id], values)

if __name__ == "__main__":
    p1 = 0
    while bits:
        if all(bit == '0' for bit in bits):
            break
        value = parse_packet()

    print('p1', p1)
    print('p2', value)