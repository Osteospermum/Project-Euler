from time import time


def digit_sum_of_power(n):
    val = str(2**n)
    array = [int(i) for i in val]
    return sum(array)


start = time()
print(digit_sum_of_power(1000))
print('Completed in', round((time() - start) * 1000), 'ms')
