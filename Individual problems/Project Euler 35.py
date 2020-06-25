from time import time


def circular_prime_count(upper_bound):
    def form_list(upper_bound):
        from itertools import product
        possible = {2}
        for n in range(1, len(str(upper_bound))):
            possible = possible | set(int(''.join(i)) for i in product('13579', repeat=n))
        return possible

    def get_shifted(n):
        result = set()
        s = str(n)
        for i in range(len(s)):
            s = s[1:]+s[0]
            result.add(int(s))
        return result

    def is_prime(n):
        from math import sqrt, ceil
        if n < 2:
            return False
        elif n != 2:
            for i in range(2, ceil(sqrt(n) + 1)):
                if n % i == 0:
                    return False
        return True

    count = 0
    possible = form_list(upper_bound)
    for n in possible:
        if all(is_prime(i) for i in get_shifted(n)):
            count += 1
    return count




start = time()
print(circular_prime_count(1000000))
print('Completed in', round((time() - start) * 1000), 'ms')
