from time import time


def consecutive_prime_sum(limit):
    def eratosthenes(limit):
        primality = [True] * limit
        primes = set()
        for i in range(2, limit):
            if primality[i - 1]:
                primes.add(i)
                for j in range(2 * i, limit, i):
                    primality[j - 1] = False
        return primes

    primes = eratosthenes(limit)
    prime_sum = [0] * len(primes)
    sorted_primes = sorted(primes)
    for i in range(1, len(primes)):
        prime_sum[i] = prime_sum[i - 1] + sorted_primes[i - 1]

    max_prime_count = 0
    max_prime_sum = 0
    for i in range(len(prime_sum) - 1, 0, -1):
        for j in range(i - max_prime_count - 1, -1, -1):
            if prime_sum[i] - prime_sum[j] > limit:
                break
            if prime_sum[i] - prime_sum[j] in primes:
                max_prime_count = i - j
                max_prime_sum = prime_sum[i] - prime_sum[j]
    return max_prime_sum


start = time()
print(consecutive_prime_sum(1000000))
print('Completed in', round((time() - start) * 1000), 'ms') 

