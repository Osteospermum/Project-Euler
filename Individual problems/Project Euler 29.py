from time import time


def powers_count(a_upto, b_upto):
    powers = set()
    for a in range(2, a_upto + 1):
        for b in range(2, b_upto + 1):
            powers.add(pow(a, b))
    print(sorted(powers))
    return len(powers)


start = time()
print(powers_count(6, 6))
print('Completed in', round((time() - start) * 1000), 'ms')
