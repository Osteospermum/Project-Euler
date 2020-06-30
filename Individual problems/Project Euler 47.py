from time import time


def consecutive_distinct_primes(count, _limit=10):
    factor_count = [0] * _limit
    for i in range(2, _limit):
        if factor_count[i] == 0:
            for j in range(2 * i, _limit, i):
                factor_count[j] += 1

    for i in range(2, _limit):
        if factor_count[i:i + count] == [count] * count:
            return i
    return consecutive_distinct_primes(count, _limit * 10)


start = time()
print(consecutive_distinct_primes(4))
print('Completed in', round((time() - start) * 1000), 'ms')

