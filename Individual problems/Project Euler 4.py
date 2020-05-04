from time import time


def find_largest_palindrome(n):
    def is_palindrome(n):
        a = str(n)[0:len(str(n)) // 2]
        b = str(n)[-(len(str(n)) // 2):]
        b = b[::-1]
        if a == b:
            return True
        return False

    x = 0
    for p in range(10 ** 3):
        for q in range(10 ** 3):
            if is_palindrome(p*q):
                if p*q > x:
                    x = p * q
    return x


start = time()
print(find_largest_palindrome(3))
print('Completed in', round((time() - start) * 1000), 'ms')
