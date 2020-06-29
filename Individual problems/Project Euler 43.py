from time import time


def divisible_pandigitals():
    def is_substring_divisible(n):
        checks = [2, 3, 5, 7, 11, 13, 17]
        for i in range(7):
            if int(n[i + 1:i + 4]) % checks[i] != 0:
                return False
        return True

    from itertools import permutations

    results = {int(''.join(i)) for i in permutations('0123465789') if is_substring_divisible(''.join(i))}
    return sum(results)


start = time()
print(divisible_pandigitals())
print('Completed in', round((time() - start) * 1000), 'ms') 

