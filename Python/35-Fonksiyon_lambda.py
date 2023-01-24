def ikiçarp(sayı):  # klasik fonkisyon
    return sayı*2


print(ikiçarp(4))
def iki_çarp(x): return x*2  # lamda lı fonksiyon


print(iki_çarp(4))


def toplama(*a):
    t = 0
    for i in a:
        t += i
    print(t)


toplam = lambda *x: sum(x)
toplama(4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
print(toplam(4, 5, 6, 7, 8, 9, 10, 11, 12, 13))
def ters_çevir(x): return x[::-1]


print(ters_çevir("merhaba"))
