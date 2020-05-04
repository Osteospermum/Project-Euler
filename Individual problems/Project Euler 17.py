from time import time


def digit_sum_of_power(n):
    # Euler 16
    val = str(2**n)
    array = [int(i) for i in val]
    return sum(array)


def num_to_word(n, no_whitespace=False):
    pwr_1 = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five',
             '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine', '10': 'ten',
             '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
             '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
    pwr_2 = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy',
             '8': 'eighty', '9': 'ninety'}
    pwr_n = ['hundred', 'thousand', 'million', 'billion', 'trillion', 'quadrillion', 'quintillion', 'sextillion'
             'septillion', 'octillion', 'nonillion', 'decillion']

    def get_short(n):
        def done(n):
            if int(n) == 0:
                return True
            return False

        answer = ''
        while n[0] == '0' and len(n) > 1:
            n = n[1:]

        while not done(n):
            if len(n) == 3:
                answer += pwr_1[n[0]]
                answer += ' '
                answer += pwr_n[0]
                n = n[1:]
                if not done(n):
                    answer += ' and '
            elif n in pwr_1:
                answer += pwr_1[n]
                break
            elif n[0] in pwr_2:
                answer += pwr_2[n[0]]
                n = n[1:]
                if not done(n):
                    answer += '-'
            else:
                n = n[1:]
        return answer

    while n[0] == '0' and len(n) > 1:
        n = n[1:]
    if n == '0':
        return 'zero'

    seperated = [n[::-1][i:i+3][::-1] for i in range(0, len(n), 3)][::-1]
    answer = ''
    for i in range(len(seperated)):
        if i == len(seperated)-1:
            answer += get_short(seperated[i])
        else:
            add = get_short(seperated[i])
            if add != '':
                answer += add
                answer += ' '
                answer += pwr_n[len(seperated) - i - 1]
                answer += ' '
    if no_whitespace:
        answer = answer.replace(' ', '')
        answer = answer.replace('-', '')
    return answer


def sum_of_numbers(n):
    length = 0
    for i in range(1, n+1):
        length += len(num_to_word(str(i), True))
    return length


start = time()
print(sum_of_numbers(1000))
print('Completed in', round((time() - start) * 1000), 'ms')
