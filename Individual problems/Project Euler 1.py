from time import time


def multiples_3_5(n):
    return_val = 0
    for i in range(3, n, 3):
        return_val += i
    for i in range(5, n, 5):
        if i % 3 != 0:
            return_val += i
    return return_val


start = time()
print(multiples_3_5(1000))
print('Completed in', round((time() - start) * 1000), 'ms')
