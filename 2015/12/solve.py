import json
data = json.loads(open('input.txt').read())

#Using new match from python 3.10

def dig_for_numbers(data):
    match data:
        case dict():
            return sum(dig_for_numbers(v) for k,v in data.items())
        case list():
            return sum(dig_for_numbers(x) for x in data)
        case int() | float():
            return data
        case str():
            return 0

def dig_for_numbers_p2(data):
    match data:
        case dict():
            if 'red' in data.values():
                return 0
            else:
                # return sum(map(dig_for_numbers_p2, data.values()))
                return sum(dig_for_numbers_p2(v) for v in data.values())
        case list():
            return sum(dig_for_numbers_p2(x) for x in data)
        case int() | float():
            return data
        case str():
            return 0


assert 10 == dig_for_numbers({'a': 10})
assert 10 == dig_for_numbers(10)
assert 6 == dig_for_numbers([1,2,3])
assert 6 == dig_for_numbers({"a":2,"b":4})
assert 3 == dig_for_numbers([[[3]]])
assert 3 == dig_for_numbers({"a":{"b":4},"c":-1})
assert 0 == dig_for_numbers({"a":[-1,1]})
assert 0 == dig_for_numbers([-1,{"a":1}])
assert 0 == dig_for_numbers([])
assert 0 == dig_for_numbers({})

print('p1', dig_for_numbers(data))

assert 4 == dig_for_numbers_p2([1,{"c":"red","b":2},3])
assert 0 == dig_for_numbers_p2({"d":"red","e":[1,2,3,4],"f":5})
assert 6 == dig_for_numbers_p2([1,"red",5])

print('p2', dig_for_numbers_p2(data))