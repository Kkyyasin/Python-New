"""Problem 3
Kullanıcıdan 2 tane sayı alarak bu sayıların en küçük ortak katlarını (EKOK) dönen bir tane fonksiyon yazın."""


def ekok_bulma(a, b):
    if a > b:
        c = a
    else:
        c = b
    while (c % a != 0) or (c % b != 0):
        c += 1
    print(c)


ekok_bulma(12, 10)
