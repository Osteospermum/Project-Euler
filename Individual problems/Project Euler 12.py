from time import time


def triangles(divisors):
    def get_triangle(n):
        return sum(list(range(1, n+1)))

    def get_divisor_count(n):
        from math import sqrt, ceil
        count = 0
        for i in range(1, ceil(sqrt(n+1))):
            if n % i == 0:
                count += 1
        return 2*count

    count = 1
    while True:
        current_triangle = get_triangle(count)
        if current_triangle >= divisors:
            if get_divisor_count(current_triangle) >= divisors:
                return current_triangle
        count += 1


start = time()
print(triangles(500))
print('Completed in', round((time() - start) * 1000), 'ms')
