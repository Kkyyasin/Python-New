# Fonksiyon Paremetreleri
# *args basındaki yıldız demet olusturu istedigimiz kadar sayı girebiliriz
# **kwargs sozluk yapısı olusturur.

def f1(*args):  # demet halde alır
    for i in args:
        print(i, end="   ")


f1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


def f2(isim, *args):
    print(isim)
    for i in args:
        print(i, end="   ")


f2("Yasin", 1, 5, 5, 4, 8, 9, 10, 11, 12, 13)


def f3(**kwards):
    print()
    for i, j in kwards.items():
        print(i, j, end=" ")


f3(isim="Mehmet", yas=18, numara=171421005)


def f4(isim, *args, **kwards):
    print("isim", isim, "\n")
    for i in args:
        print(i, end="  ")
    for i, j in kwards.items():
        print(i, j, end="  ")


f4("Yasin", 1, 5, 5, 4, 8, a="Mehmet", yas=21, num=446)
a = {"isiam": "Mhe", "Yas": 44, "num": 778}
b = [*range(10)]
c = "mehmet"
f4(c, *b, **a)
#!fonksiyondaki degisken ismi ile sozlukdeki anahtar ismi aynı olmaz.yoksa type error hatası alınır yani sozluktedi isimle fonsiyon paremetresi isim aynı olamaz.


def selamla(isim):
    print("Merhaba", isim)


selamla("Yasin")
print(selamla)
merhaba = selamla  # fonsiyon eşitlenir
merhaba("Mehmet")
print(merhaba)
del selamla  # ?objenin silinmesine yarar del
merhaba("mustafa")  # obje silinsede yinede çalışır


# ?İç içe fonksiyon
def fonk1():
    def fonk2():  # !Local fonksiyon dışardan erişelemez fonksiyon bittiğinde silinir
        print("fonk2")
    fonk2()
    print("fonk1")


def fonksiyon(*args):
    def toplama(args):
        sum = 0
        for i in args:
            sum += i
        return sum
    print(toplama(args))


fonksiyon(15, 8, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)
