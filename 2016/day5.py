from hashlib import md5
from itertools import count

prefix = 'reyedfim'
#prefix = 'abc'
password = {}

for num in count():
    code = str(prefix + str(num)).encode('utf8')
    h = md5(code).hexdigest()

    if h.startswith('00000'):
        index = h[5]

        if index in '01234567':
            index = int(index)

            if index not in password:
                password[index] = h[6]

                if len(password) == 8:
                    break

# Print the password in correct order.
for i in range(8):
    print(password[i], end='')