from functools import reduce
# ilk önce ilk iki değer işleme alınıyor.sonra sonuç bir sonraki değerle işleme alınıyor
print(reduce(lambda x, y: x + y, [1, 2, 3, 4, 5]))
print(reduce(lambda x, y: x * y, [1, 2, 3, 4, 5]))  # faktoriyel yarıyor


def max(x, y):
    if x < y:
        return y
    else:
        return x


print(reduce(max, [1, 2, 3, 5, 7, 8, 1, 6]))  # max bulmaya yarıyor
