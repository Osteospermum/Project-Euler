from time import time


def prime_permutations(n):
    def is_prime(n):
        from math import sqrt, ceil
        if n < 2:
            return False
        elif n != 2:
            for i in range(2, ceil(sqrt(n) + 1)):
                if n % i == 0:
                    return False
        return True

    def is_permutations(nums):
        sorted_nums = [sorted(str(i)) for i in nums]
        return sorted_nums.count(sorted_nums[0]) == len(sorted_nums)

    results = set()
    primes = set()
    for i in range(10 ** (n-1), 10 ** n):
        if is_prime(i):
            primes.add(i)
    for num in primes:
        increment = 2
        while num + 2 * increment < 10 ** n:
            if num + increment in primes and num + 2 * increment in primes:
                if is_permutations([num + i * increment for i in range(3)]):
                    results.add(tuple(num + i * increment for i in range(3)))
            increment += 2

    return [''.join(str(i) for i in answer) for answer in results if answer[0] != 1487][0]


start = time()
print(prime_permutations(4))
print('Completed in', round((time() - start) * 1000), 'ms') 

