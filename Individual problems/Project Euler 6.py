import time


def sum_square_dif(n):
    sum_of_squares = 0
    for i in range(1, n+1):
        sum_of_squares += i*i
    sum_squared = 0
    for i in range(1, n+1):
        sum_squared += i
    sum_squared *= sum_squared
    return sum_squared - sum_of_squares


start = time.time()
print(sum_square_dif(100))
print('Completed in', round((time() - start)*1000), 'ms')
