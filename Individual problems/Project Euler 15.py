from time import time


def route_counter(size):
    map = [[0 for k in range(size + 1)] for i in range(size + 1)]
    for i in range(size + 1):
        map[i][-1] = 1
        map[-1][i] = 1
    map[-1][-1] = 0
    map[-2][-2] = 2
    if size > 2:
        for i in range(size-1, -1, -1):
            for k in range(size-1, -1, -1):
                map[i][k] = map[i+1][k] + map[i][k+1]
    return map[0][0]


start = time()
print(route_counter(20))
print('Completed in', round((time() - start) * 1000), 'ms')
