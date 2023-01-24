"""Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise *return* ile bu değeri dönsün. Ancak sayı tek sayı ise fonksiyon *raise* ile *ValueError* hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın."""


def sayiKontrol(a):
    try:
        if a % 2 != 0:
            raise ValueError("{} sayisi çift    değildir".format(a))
        return a
    except ValueError as e:
        print(e)


liste = [*range(100)]
n = []
for i in liste:
    if None != sayiKontrol(i):
        n.append(i)
for i in n:
    print(i)
