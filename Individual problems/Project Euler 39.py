from time import time


def maximum_right_triangle(max_perimeter):
    def primitive_pythagorean_triplet(perimeter):
        from math import floor, sqrt, gcd
        if not (perimeter / 2).is_integer():
            return 0
        count = 0
        for m in range(2, floor(sqrt(perimeter // 2))):
            n = (perimeter / 2 - m * m) / m
            if n.is_integer() and 0 < n < m:
                n = int(n)
                if gcd(m, n) == 1 and (m % 2 == 0 or n % 2 == 0):
                    count += 1
        return count

    def primitive_dictionary_upto(max_perimeter):
        result = {}
        for i in range(1, max_perimeter + 1):
            triplet_count = primitive_pythagorean_triplet(i)
            if triplet_count > 0:
                result[i] = triplet_count
        return result

    perimeter_dictionary = primitive_dictionary_upto(max_perimeter)
    primitive_perimeters = list(perimeter_dictionary.keys())
    all_perimeters = []
    for current in range(1, max_perimeter + 1):
        count = 0
        for primitive in primitive_perimeters:
            if primitive > current:
                break
            if current % primitive == 0:
                count += perimeter_dictionary[primitive]
        all_perimeters.append(count)

    return all_perimeters.index(max(all_perimeters)) + 1


start = time()
print(maximum_right_triangle(1000))
print('Completed in', round((time() - start) * 1000), 'ms') 

