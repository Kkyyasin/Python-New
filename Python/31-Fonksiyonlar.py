def selamla():
    print("Merhaba nasılsın ")


print(type(selamla))
selamla()
selamla()


def merhaba(isim):
    print("Merhaba", isim)


merhaba("Ahmet")


def toplam(a, b, c):
    print("Toplam", a+b+c)


toplam(3, 4, 5)


def faktoreyel(sayi):
    faktoreyel = 1
    if sayi == 0 or sayi == 1:
        faktoreyel = 1
    else:
        while sayi > 1:
            faktoreyel *= sayi
            sayi -= 1
    print("Faktoreyel:", faktoreyel)


faktoreyel(0)
