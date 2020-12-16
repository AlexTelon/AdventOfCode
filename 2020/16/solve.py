from collections import defaultdict, Counter
import itertools
from itertools import product, permutations, combinations, repeat, count
import queue
from threading import Thread
from collections import deque
from decimal import Decimal
from fractions import Fraction
import fractions
# import networkx
import string
import operator

## Alphabet
# alphas = string.ascii_lowercase 
# product('ABCD', repeat=2)                 -> AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# permutations('ABCD', 2)                   -> AB AC AD BA BC BD CA CB CD DA DB DC
# combinations('ABCD', 2)                   -> AB AC AD BC BD CD
# combinations_with_replacement('ABCD', 2)  -> AA AB AC AD BB BC BD CC CD DD

departure_location = [(32,209), (234,963)]
departure_station = [(47,64), (83,967)]
departure_platform = [(37,609), (628,970)]
departure_track = [(29,546), (567,971)]
departure_date = [(50,795), (816,960)]
departure_time = [(49,736), (750,962)]
arrival_location = [(48,399), (420,967)]
arrival_station = [(49,353), (360,967)]
arrival_platform = [(37,275), (298,969)]
arrival_track = [(40,119), (127,954)]
class_ = [(35,750), (760,968)]
duration = [(43,162), (186,963)]
price = [(30,889), (914,949)]
route = [(39,266), (274,950)]
row = [(45,366), (389,954)]
seat = [(42,765), (772,955)]
train = [(30,494), (518,957)]
type_ = [(48,822), (835,973)]
wagon = [(32,330), (342,951)]
zone = [(36,455), (462,973)]

rules = [departure_location, departure_station, departure_platform, departure_track, departure_date, departure_time, arrival_location, arrival_station, arrival_platform, arrival_track, class_, duration, price, route, row, seat, train, type_, wagon, zone]

# mine:
my_ticket = [109,137,131,157,191,103,127,53,107,151,61,59,139,83,101,149,89,193,113,97]

def check_num_against_rules(x):
    for ranges in rules:
        if any(lo <= x <= hi for lo, hi in ranges):
            return True
    return False
        # for ranges in rule:
        #     print(ranges)

# lines = open('input.txt').read().splitlines()
lines = open(0).read().splitlines()
# lines = [(int(x), i+1) for i,x in enumerate(lines)]
lines = [[int(x) for x in line.split(',')] for line in lines]
passing, failing = 0,0
for line in lines:
    for x in line:
        if not check_num_against_rules(x):
            failing += x
    # if all(check_num_against_rules(x) for x in line):
    #     passing += 1
    # else:
    #     failing += x
# print("pass", passing)
print("fail", failing)

    