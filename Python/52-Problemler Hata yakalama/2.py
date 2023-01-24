"""Bir sayının çift olup olmadığını sorgulayan bir fonksiyon yazın. Bu fonksiyon, eğer sayı çift ise return ile bu değeri dönsün. Ancak sayı tek sayı ise fonksiyon raise ile ValueError hatası fırlatsın. Daha sonra, içinde çift ve tek sayılar bulunduran bir liste tanımlayın ve liste üzerinde gezinerek ekrana sadece çift sayıları bastırın."""


def çiftmi_tekmi(sayı):
    if sayı % 2 == 0:
        return sayı
    else:
        raise ValueError("Tek sayı")


liste = [i for i in range(20)]
for i in liste:
    try:
        print(çiftmi_tekmi(i))
    except ValueError:
        print("Tek sayı")
