from time import time


def powers_count(a_upto, b_upto):
    powers = set()
    for a in range(2, a_upto + 1):
        for b in range(2, b_upto + 1):
            powers.add(pow(a, b))
    return len(powers)


start = time()
print(powers_count(100, 100))
print('Completed in', round((time() - start) * 1000), 'ms')
