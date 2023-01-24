def double(x):
    return x*2


print(list(map(double, [1, 2, 3, 4])))  # fonksiyon ,iterotor
print(list(map(lambda x: x*3, [1, 2, 3, 4])))
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]
l3 = [9, 10, 11, 12, 13]
print(list(map(lambda x, y: x*y, l1, l2)))
# sadece 4 değr yazdırır 13 karşısında değer olmadığı için yazmaz
print(list(map(lambda x, y, z: x*y*z, l1, l2, l3)))
