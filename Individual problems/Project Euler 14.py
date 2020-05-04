from time import time


def collatz_length(start):
    length = 1
    n = start
    while n != 1:
        if n % 2 == 0:
            n /= 2
        else:
            n = 3 * n + 1
        length += 1
    return length


def collatz(under):
    from multiprocessing import Pool
    if __name__ == '__main__':
        with Pool(15) as p:
            collatz_list = p.map(collatz_length, range(1, under))
        return collatz_list.index(max(collatz_list)) + 1


if __name__ == '__main__':
    start = time()
    print(collatz(1000000))
    print('Completed in', round((time() - start) * 1000), 'ms')
