from time import time


def find_prime_factors(n):
    num = n
    factors = []

    def is_prime(m):
        from math import sqrt, floor
        if m > 2:
            for i in range(2, floor(sqrt(m)) + 1):
                if m % i == 0:
                    return False
        return True

    while not is_prime(num):
        for i in range(2, num):
            if is_prime(i):
                if num % i == 0:
                    num = int(num / i)
                    factors.append(i)
                    break
    factors.append(num)
    return max(factors)


start = time()
print(find_prime_factors(600851475143))
print('Completed in', round((time() - start) * 1000), 'ms')
