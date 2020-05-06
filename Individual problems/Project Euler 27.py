from time import time


class Formula:
    def __init__(self, ia, ib):
        self.a = ia
        self.b = ib

    def consecutive_primes(self):
        def is_prime(m):
            from math import sqrt, floor
            if m > 2:
                for i in range(2, floor(sqrt(m)) + 1):
                    if m % i == 0:
                        return False
            else:
                return False
            return True

        count = 0
        result = count * count + self.a * count + self.b
        while is_prime(result):
            count += 1
            result = count * count + self.a * count + self.b
        return count


def find_max_product(ab_max):
    def is_prime(m):
        from math import sqrt, floor
        if m > 2:
            for i in range(2, floor(sqrt(m)) + 1):
                if m % i == 0:
                    return False
        else:
            return False
        return True
    f = Formula(0, 0)
    best = (0, 0, 0)
    for b in range(1, ab_max + 1):
        if not is_prime(b):
            continue
        f.b = b
        for a in range(-ab_max, ab_max):
            f.a = a
            if f.consecutive_primes() > best[0]:
                best = (f.consecutive_primes(), f.a, f.b)
    print(best)
    return best[1] * best[2]


start = time()
print(find_max_product(1000))
print('Completed in', round((time() - start) * 1000), 'ms')
