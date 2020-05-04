from time import time


def sundays(start_year, end_year, first_day=1):
    current_day = first_day
    count = 0
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    for current_year in range(start_year, end_year + 1):
        for current_month in range(len(month_days)):
            if current_day == 0:
                count += 1
            if current_month == 1 and \
                ((current_year % 4 == 0 and not current_year % 100 == 0) or (current_year % 400 == 0)):
                current_day += 29 % 7
            else:
                current_day += month_days[current_month] % 7
            current_day %= 7
    return count


start = time()
print(sundays(1901, 2000, 0))
print('Completed in', round((time() - start) * 1000), 'ms')
