from time import time


def smallest_multiple(n):
    def multiple_of(n, nums):
        for i in nums:
            if n % i != 0:
                return False
        return True

    multiple = 1
    for i in range(n):
        multiple *= (i+1)
    while True:
        original = multiple
        for i in range(1, n):
            if multiple % (i+1) == 0:
                new_multiple = multiple / (i + 1)
                if multiple_of(new_multiple, range(2, n + 1)):
                    multiple /= (i+1)
        if original == multiple:
            break
    return int(multiple)


start = time()
print(smallest_multiple(20))
print('Completed in', round((time() - start) * 1000), 'ms')
