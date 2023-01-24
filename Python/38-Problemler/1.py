"""Problem 1
1'den 1000'e kadar olan sayılardan mükemmel sayı olanları ekrana yazdırın. Bunun için bir sayının mükemmel olup olmadığını dönen bir tane fonksiyon yazın.

Bir sayının bölenlerinin toplamı kendine eşitse bu sayı mükemmel bir sayıdır. Örnek olarak 6 mükemmel bir sayıdır (1 + 2 + 3 = 6)."""


def mükemmel_sayi_kontrol(sayi):
    t = 0
    print("{} sayısı ".format(sayi), end="")
    for i in range(1, sayi):
        if sayi % i == 0:
            t += i
    if t == sayi:
        print("Mükemmel sayıdır")
    else:
        print("Mükemmel sayı değildir")


for i in range(1, 1001):
    mükemmel_sayi_kontrol(i)
