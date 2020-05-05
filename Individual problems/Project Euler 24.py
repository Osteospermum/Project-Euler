from time import time


def lexicographic_permutation(size, index):
    from itertools import permutations
    return ''.join(str(i) for i in list(permutations(range(size)))[index-1])


start = time()
print(lexicographic_permutation(10, 1000000))
print('Completed in', round((time() - start) * 1000), 'ms')
