from time import time


def triangle_word_count(target_file):
    def next_triangle():
        n = len(triangles)
        triangles.append(n * (n + 1) // 2)

    from string import ascii_uppercase
    triangles = [1]
    count = 0
    with open(target_file, 'r') as f:
        words = f.readline().replace('"', '').split(',')
    for word in words:
        value = sum(ascii_uppercase.index(i) + 1 for i in word)
        while value > triangles[-1]:
            next_triangle()
        if value in triangles:
            count += 1
    return count


start = time()
print(triangle_word_count('Project Euler 42 words.txt'))
print('Completed in', round((time() - start) * 1000), 'ms') 

