from time import time


def amicable_sum(n):
    def is_amicable(n):
        def sum_divisors(n):
            from math import ceil, sqrt
            return_val = 0
            for i in range(2, ceil(sqrt(n))):
                if n % i == 0:
                    return_val += i + (n / i)
            return int(return_val + 1)

        pair = sum_divisors(n)
        if pair != n and sum_divisors(pair) == n:
            return True
        return False

    return_val = 0
    for i in range(1, n):
        if is_amicable(i):
            return_val += i
    return return_val


start = time()
print(amicable_sum(10000))
print('Completed in', round((time() - start) * 1000), 'ms')

