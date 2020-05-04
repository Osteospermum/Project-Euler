from time import time


def factorial_digit_sum(n):
    def factorial(n):
        if n == 1:
            return 1
        return n * factorial(n - 1)

    digits = [int(i) for i in str(factorial(n))]
    return sum(digits)


start = time()
print(factorial_digit_sum(100))
print('Completed in', round((time() - start) * 1000), 'ms')
