from time import time


def eratosthenes(n):
    primes = [True for i in range(n)]
    primes[0] = False
    for i in range(2, n):
        if primes[i-1]:
            for k in range(2 * i, n+1, i):
                if primes[k-1]:
                    primes[k-1] = False
    return_sum = 0
    for i in range(n):
        if primes[i]:
            return_sum += i+1
    return return_sum


start = time()
print(eratosthenes(2000000))
print('Completed in', round((time() - start) * 1000), 'ms')
