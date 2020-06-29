from time import time


def product_counter(n):
    products = set()
    num_set = set('123456789'[:n])
    for a in range(10000):
        for b in range(1000):
            if len(str(a)) + len(str(b)) + len(str(a*b)) > n:
                break
            if set(str(a) + str(b) + str(a*b)) == num_set:
                products.add(a*b)
    return sum(products)


start = time()
print(product_counter(9))
print('Completed in', round((time() - start) * 1000), 'ms')
