from time import time


def champernowne_digits(max_power):
    s = ''
    i = 1
    while len(s) <= 10 ** max_power:
        s += str(i)
        i += 1
    result = 1
    j = 1
    while j <= max_power:
        result *= int(s[10 ** j - 1])
        j += 1
    return result


start = time()
print(champernowne_digits(6))
print('Completed in', round((time() - start) * 1000), 'ms') 

