from time import time


def fibonacci_sum(n):
    def fibonacci(n):
        a, b = 0, 1
        sequence = []
        while a < n:
            a, b = b, a + b
            sequence.append(a)
        return sequence

    total = 0
    for i in fibonacci(n):
        if i % 2 == 0:
            total += i
    return total


start = time()
print(fibonacci_sum(4000000))
print('Completed in', round((time() - start) * 1000), 'ms')
