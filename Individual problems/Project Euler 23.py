from time import time


def is_abundant(n):
    from math import sqrt, floor
    div_sum = 1
    for i in range(2, floor(sqrt(n)) + 1):
        if n % i == 0:
            div_sum += i + (n / i if i * i != n else 0)
    if div_sum > n:
        return True
    return False





def worker_function(args):
    num, abundants = args
    def is_summed_abundant(num):
        for i in abundants:
            if i > num / 2:
                return False
            elif num - i in abundants:
                return True
        return False

    if num < 24 or not is_summed_abundant(num):
        return num
    else:
        return 0


if __name__ == '__main__':
    start = time()

    abundants = []
    upto = 28123
    for i in range(1, upto):
        if is_abundant(i):
            abundants.append(i)

    from multiprocessing import Pool
    with Pool(30) as p:
        unsummables = p.map(worker_function, zip(range(1, upto + 1), [abundants for i in range(upto)]))
    print(sum(unsummables))

    print('Completed in', round((time() - start) * 1000), 'ms')
