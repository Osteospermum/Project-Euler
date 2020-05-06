from time import time


class DigitCrawler:
    def __init__(self, power):
        self.power = power
        self.pos = 0
        self.digit_count = 1
        self.count = 0
        self.total = 0
        while len(str(9 ** self.power * self.digit_count)) > self.digit_count:
            self.digit_count += 1
        self.max_number = 9 ** self.power * self.digit_count
        self.current_digits = ['0' for i in range(self.digit_count)]

    def crawl(self):
        for i in range(10):
            self.current_digits[self.pos] = str(i)
            if int(''.join(self.current_digits)) > self.max_number:
                return self.total
            if self.pos == self.digit_count - 1:
                if int(''.join(self.current_digits)) == sum(int(n) ** self.power for n in self.current_digits)\
                        and int(''.join(self.current_digits)) != 0 and int(''.join(self.current_digits)) != 1:
                    self.count += 1
                    self.total += int(''.join(self.current_digits))
            else:
                self.pos += 1
                self.crawl()
        self.pos -= 1
        return self.total


start = time()
dc = DigitCrawler(5)
print(dc.crawl())
print('Completed in', round((time() - start) * 1000), 'ms')
