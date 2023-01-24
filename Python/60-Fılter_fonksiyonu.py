# filter metodu sadece true false donduren fonksiyonlarda çalışır
print(list(filter(lambda x: x % 2 == 0, [1, 2, 5, 6, 6])))


def asal(x):
    if (x == 0 or x == 1):
        return False
    for i in range(2, x):
        if x % i == 0:
            return False
    return True


print(list(filter(asal, range(100))))
