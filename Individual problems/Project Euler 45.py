from time import time


def last_triple_number(count):
    from math import sqrt

    def is_triangle(n):
        return (-1 + sqrt(1 + 8 * n)) % 2 == 0

    def is_pentagonal(n):
        return (1 + sqrt(1 + 24 * n)) % 6 == 0

    index = 1
    num = index * (2 * index - 1)
    current = 0
    while current < count:
        index += 1
        num = index * (2 * index - 1)
        if is_triangle(num) and is_pentagonal(num):
            current += 1
    return num


start = time()
print(last_triple_number(2))
print('Completed in', round((time() - start) * 1000), 'ms') 

