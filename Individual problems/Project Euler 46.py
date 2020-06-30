from time import time


def minimum_goldbach():
    def is_prime(n):
        from math import sqrt, ceil
        if n < 2:
            return False
        elif n != 2:
            for i in range(2, ceil(sqrt(n) + 1)):
                if n % i == 0:
                    return False
        return True

    from math import ceil, sqrt

    num = 3
    while True:
        if not any(is_prime(num - 2 * i * i) for i in range(ceil(sqrt(num)))):
            return num
        num += 2


start = time()
print(minimum_goldbach())
print('Completed in', round((time() - start) * 1000), 'ms') 

