from time import time


def non_trivial_fractions(digits):
    from math import gcd
    numerator, denominator = 1, 1
    for a in range(10 ** (digits - 1), 10 ** digits):
        if '0' not in str(a):
            for b in range(a + 1, 10 ** digits):
                if any(i in str(a) for i in str(b)) and '0' not in str(b):
                    i = list(set(str(a)) & set(str(b)))[0]
                    x = list(str(a))
                    x.remove(i)
                    at = int(''.join(x))
                    x = list(str(b))
                    x.remove(i)
                    bt = int(''.join(x))
                    if at / bt == a / b:
                        numerator *= at
                        denominator *= bt
    return denominator // gcd(numerator, denominator)


start = time()
print(non_trivial_fractions(2))
print('Completed in', round((time() - start) * 1000), 'ms')
