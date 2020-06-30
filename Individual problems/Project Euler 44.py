from time import time


def pentagonal_pair():
    index = 1
    pentagons = {1}
    while True:
        index += 1
        n = index * (3 * index - 1) // 2
        pentagons.add(n)
        for k in pentagons:
            if n - k in pentagons and n - 2 * k in pentagons:
                return n - 2 * k


start = time()
print(pentagonal_pair())
print('Completed in', round((time() - start) * 1000), 'ms') 

