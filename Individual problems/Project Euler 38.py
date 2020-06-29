from time import time


def largest_pandigital(minimum_n):
    from math import ceil
    i = 1
    curr_max = 0
    number_set = set('123456789')
    while i < 10 ** ceil(9 / minimum_n):
        n = 0
        num = ''
        while n < minimum_n or len(num) < 9:
            n += 1
            num += str(n * i)
            if len(num) == 9 and set(num) == number_set and int(num) > curr_max:
                curr_max = int(num)
        i += 1
    return curr_max


start = time()
print(largest_pandigital(2))
print('Completed in', round((time() - start) * 1000), 'ms')
