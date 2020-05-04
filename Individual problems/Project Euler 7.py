from time import time
prime_list = [2, 3]


# Miller Raibin primality test taken from Rosetta Code
# https://rosettacode.org/wiki/Miller%E2%80%93Rabin_primality_test#Python:_Proved_correct_up_to_large_N
def miller_raibin(n, _precision_for_huge_n=16):
    def _try_composite(a, d, n, s):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True  # n  is definitely composite

    if n in prime_list:
        return True
    if any((n % p) == 0 for p in prime_list[:25]) or n in (0, 1):
        return False
    d, s = n - 1, 0
    while not d % 2:
        d, s = d >> 1, s + 1
    # Returns exact according to http://primes.utm.edu/prove/prove2_3.html
    if n < 1373653:
        return not any(_try_composite(a, d, n, s) for a in (2, 3))
    if n < 25326001:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5))
    if n < 118670087467:
        if n == 3215031751:
            return False
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7))
    if n < 2152302898747:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11))
    if n < 3474749660383:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13))
    if n < 341550071728321:
        return not any(_try_composite(a, d, n, s) for a in (2, 3, 5, 7, 11, 13, 17))
    # otherwise
    return not any(_try_composite(a, d, n, s)
                   for a in prime_list[:_precision_for_huge_n])


def find_prime_at(n):
    count = prime_list[-1] + 1
    while len(prime_list) < n:
        if miller_raibin(count):
            prime_list.append(count)
        count += 1
    return prime_list[-1]


start = time()
print(find_prime_at(10001))
print('Completed in', round((time() - start) * 1000), 'ms')
