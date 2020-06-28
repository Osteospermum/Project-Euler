from time import time


def find_truncatable_primes(count):
    def is_prime(n):
        from math import sqrt, ceil
        if n < 2:
            return False
        elif n != 2:
            for i in range(2, ceil(sqrt(n) + 1)):
                if n % i == 0:
                    return False
        return True

    def is_truncatable_left_prime(n):
        if is_prime(n):
            if n >= 10:
                return is_truncatable_left_prime(int(str(n)[1:]))
            else:
                return True
        return False

    def is_truncatable_right_prime(n):
        if is_prime(n):
            if n >= 10:
                return is_truncatable_right_prime(int(str(n)[:-1]))
            else:
                return True
        return False

    i = 11
    nums = set()
    while len(nums) < count:
        if not any(c in ('' if i < 100 else '024568') for c in str(i)):
            if is_truncatable_left_prime(i) and is_truncatable_right_prime(i):
                nums.add(i)
        i += 2
    return sum(nums)


start = time()
print(find_truncatable_primes(11))
print('Completed in', round((time() - start) * 1000), 'ms')
