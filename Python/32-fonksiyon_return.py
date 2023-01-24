def toplama(a, b, c):
    return a+b+c


def üs_al(a, x):

    print(a**x)


toplam = toplama(3, 4, 5)
üs_al(toplam, 2)


def üçleçarp(a):
    print("1-fonksiyon çalıştı")
    return a*3


def dördeböl(a):
    print("2-fonksiyon çalıştı")
    return a/4


def kareal(a):
    print("3-fonksiyon  çalıştı")
    a*2
    print(a)


kareal(dördeböl(üçleçarp(3)))
