from time import time


def largest_repeating(upto):
    def find_repeating(num):
        """Find number of repeating digits of 1/num based of of Fermat's Little theorem"""
        k = 1
        while 10**k % num != 1:
            k += 1
        return k

    def is_prime(m):
        from math import sqrt, floor
        if m > 2:
            for i in range(2, floor(sqrt(m)) + 1):
                if m % i == 0:
                    return False
        else:
            return False
        return True

    numbers = []
    repeating_count = []
    for i in range(10, upto):
        if is_prime(i):
            numbers.append(i)
            repeating_count.append(find_repeating(i))
    return numbers[repeating_count.index(max(repeating_count))]


start = time()
print(largest_repeating(1000))
print('Completed in', round((time() - start) * 1000), 'ms')
