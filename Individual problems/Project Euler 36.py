from time import time


def sum_binary_palindrome(upper_bound):
    def is_palindrome(n):
        if len(str(n)) < 2:
            return True
        a = str(n)[0:len(str(n)) // 2]
        b = str(n)[-(len(str(n)) // 2):]
        b = b[::-1]
        if a == b:
            return True
        return False

    result = 0
    for i in range(upper_bound):
        if is_palindrome(i):
            if is_palindrome(bin(i)[2:]):
                result += i
    return result


start = time()
print(sum_binary_palindrome(1000000))
print('Completed in', round((time() - start) * 1000), 'ms')
