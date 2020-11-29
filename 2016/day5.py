from hashlib import md5

prefix = 'reyedfim'
#prefix = 'abc
password = ""
index = 0

while True:

    code = str(prefix + str(index)).encode('utf8')
    index += 1
    h = md5(code).hexdigest()

    if h.startswith('00000'):
        password += h[5]
        
        if len(password) == 8:
            break

print(h)
print(password)