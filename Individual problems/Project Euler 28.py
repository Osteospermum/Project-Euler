from time import time


def spiral_diag_sum(size):
    size = int((size + 1) / 2)
    diagonals = {1}
    for i in range(1, size):
        for k in range(4):
            diagonals.add(max(diagonals) + 2 * i)
    return sum(diagonals)


start = time()
print(spiral_diag_sum(1001))
print('Completed in', round((time() - start) * 1000), 'ms')
