rules = {
    'departure_location': lambda x: any(lo <= x <= hi for lo, hi in [(32,209), (234,963)]),
    'departure_station': lambda x: any(lo <= x <= hi for lo, hi in [(47,64), (83,967)]),
    'departure_platform': lambda x: any(lo <= x <= hi for lo, hi in [(37,609), (628,970)]),
    'departure_track': lambda x: any(lo <= x <= hi for lo, hi in [(29,546), (567,971)]),
    'departure_date': lambda x: any(lo <= x <= hi for lo, hi in [(50,795), (816,960)]),
    'departure_time': lambda x: any(lo <= x <= hi for lo, hi in [(49,736), (750,962)]),
    'arrival_location': lambda x: any(lo <= x <= hi for lo, hi in [(48,399), (420,967)]),
    'arrival_station': lambda x: any(lo <= x <= hi for lo, hi in [(49,353), (360,967)]),
    'arrival_platform': lambda x: any(lo <= x <= hi for lo, hi in [(37,275), (298,969)]),
    'arrival_track': lambda x: any(lo <= x <= hi for lo, hi in [(40,119), (127,954)]),
    'class': lambda x: any(lo <= x <= hi for lo, hi in [(35,750), (760,968)]),
    'duration': lambda x: any(lo <= x <= hi for lo, hi in [(43,162), (186,963)]),
    'price': lambda x: any(lo <= x <= hi for lo, hi in [(30,889), (914,949)]),
    'route': lambda x: any(lo <= x <= hi for lo, hi in [(39,266), (274,950)]),
    'row': lambda x: any(lo <= x <= hi for lo, hi in [(45,366), (389,954)]),
    'seat': lambda x: any(lo <= x <= hi for lo, hi in [(42,765), (772,955)]),
    'train': lambda x: any(lo <= x <= hi for lo, hi in [(30,494), (518,957)]),
    'type': lambda x: any(lo <= x <= hi for lo, hi in [(48,822), (835,973)]),
    'wagon': lambda x: any(lo <= x <= hi for lo, hi in [(32,330), (342,951)]),
    'zone': lambda x: any(lo <= x <= hi for lo, hi in [(36,455), (462,973)]),
}
# 109,137,131,157,191,103,127,53,107,151,61,59,139,83,101,149,89,193,113,97

lines = open('input.txt').read().splitlines()
lines = [[int(x) for x in line.split(',')] for line in lines]

ans = 0
for line in lines:
    for x in line:
        if not any(rule(x) for rule in rules.values()):
            ans += x
print(ans)