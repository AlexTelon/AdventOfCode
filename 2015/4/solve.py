from hashlib import md5
import itertools

secret = "iwrupvqb"

for i in itertools.count():
    key = secret + str(i)
    key = key.encode('utf-8')
    hashed = md5(key).hexdigest()
    # part 1
    # if hashed[:6] == "000000":
    if hashed[:6] == "000000":
        print(key)
        print(i)
        exit()