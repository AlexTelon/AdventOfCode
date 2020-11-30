from hashlib import md5
from itertools import count
from multiprocessing import Process, Queue

prefix = 'reyedfim'
#prefix = 'abc'

def reader(queue):
    password = {}
    while True:
        index, num, value = queue.get()
        # print(index, num, value)
        if index not in password:
            password[index] = (value, num)
        else:
            _, prev_num = password[index]
            if prev_num > num:
                password[index] = (value, num)

        if len(password) == 8:
            for i in range(8):
                print(password[i][0], end='')
            return


def solve(prefix, pqueue, num, step):
    password = {}
    for num in count(start=num, step=step):
        code = str(prefix + str(num)).encode('utf8')
        h = md5(code).hexdigest()

        if h.startswith('00000'):
            index, value = h[5], h[6]

            if index in '01234567':
                index = int(index)
                pqueue.put((index, num, value))

    return password

if __name__ == '__main__':
    pqueue = Queue() # writer() writes to pqueue from _this_ process
    reader_p = Process(target=reader, args=((pqueue),))
    reader_p.daemon = True
    reader_p.start()
    
    
    N = 8
    print(N)
    for i in range(N):
        derp = Process(target=solve, args=((prefix, pqueue, i, N)))
        derp.daemon = True
        derp.start()

    # solve_odd = Process(target=solve, args=((prefix, pqueue, 1, 4)))
    # solve_odd.daemon = True
    # solve_odd.start()

    # solve_odd3 = Process(target=solve, args=((prefix, pqueue, 2, 4)))
    # solve_odd3.daemon = True
    # solve_odd3.start()

    # solve_odd4 = Process(target=solve, args=((prefix, pqueue, 3, 4)))
    # solve_odd4.daemon = True
    # solve_odd4.start()

    reader_p.join()