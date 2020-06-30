from time import time


def last_self_power(limit, digit_count):
    return str(sum(i ** i for i in range(1, limit + 1)))[-digit_count:]


start = time()
print(last_self_power(1000, 10))
print('Completed in', round((time() - start) * 1000), 'ms') 

