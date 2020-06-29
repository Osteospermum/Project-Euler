from time import time


def max_pandigital_prime(n_max=9):
    def is_prime(n):
        from math import sqrt, ceil
        if n < 2:
            return False
        elif n != 2:
            for i in range(2, ceil(sqrt(n) + 1)):
                if n % i == 0:
                    return False
        return True

    from itertools import permutations
    number_set = '123456789'[:n_max]
    possibles = sorted([int(''.join(i)) for i in permutations(number_set, n_max)])[::-1]
    for i in possibles:
        if is_prime(i):
            return i
    return max_pandigital_prime(n_max - 1)


start = time()
print(max_pandigital_prime())
print('Completed in', round((time() - start) * 1000), 'ms') 

