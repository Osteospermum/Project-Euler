from time import time


def find_score(target_file):
    from string import ascii_uppercase
    f = open(target_file, 'r')
    names = sorted(f.readline().replace('"', '').split(','))
    points = []
    for n in range(len(names)):
        points.append(sum([ascii_uppercase.index(i) + 1 for i in names[n]]) * (n+1))
    return sum(points)


start = time()
print(find_score('Project Euler 22 names.txt'))
print('Completed in', round((time() - start) * 1000), 'ms')
