from time import time


def count_ways(total, coins=(1, 2, 5, 10, 20, 50, 100, 200)):
    ways = [0 for i in range(total + 1)]
    ways[0] = 1
    for n in coins:
        for i in range(n, total + 1):
            ways[i] += ways[i - n]
    return ways[total]

start = time()
print(count_ways(200))
print('Completed in', round((time() - start) * 1000), 'ms')
