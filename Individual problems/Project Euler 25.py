from time import time


def fibonacci(length):
    a, b = 1, 1
    index = 1
    while len(str(a)) < length:
        a, b = b, a + b
        index += 1
    return index


start = time()
print(fibonacci(1000))
print('Completed in', round((time() - start) * 1000), 'ms')
