from time import time


def pythagorean_triplet(total):
    from math import sqrt
    for b in range(1, total):
        for a in range(1, total):
            c = sqrt(a * a + b * b)
            if a + b + c == 1000:
                return int(a * b * c)


start = time()
print(pythagorean_triplet(1000))
print('Completed in', round((time() - start) * 1000), 'ms')
