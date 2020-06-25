from time import time


def fact(n):
    if n <= 1:
        return 1
    return fact(n - 1) * n


def sum_factorial_digits():
    # The maximum sum is made up entirely of 9!, where 9! * n has n digits
    # This equation holds true for n = 7 with result of 2 540 160
    # (Note that no number will reach this upper limit as 9 999 999 is significantly more than
    # 2 540 160 the 9! * 7, but it will mark our upper limit regardless)
    # Since we know the upper bound for a 7 digit number is 2 540 160 we can find a lower upper bound
    # When the number is 1 999 999, or 9! * 6 + 1 = 2 177 281
    factorials = [fact(i) for i in range(10)]
    result = 0
    for n in range(10, 2177281):
        if sum(factorials[int(i)] for i in str(n)) == n:
            result += n
    return result


start = time()
print(sum_factorial_digits())
print('Completed in', round((time() - start) * 1000), 'ms')
