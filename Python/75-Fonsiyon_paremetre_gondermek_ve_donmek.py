# Fonksiyonları donmek
def anafonksiyon(islemadi):
    def carpma(*args):
        c = 1
        for i in args:
            c *= i
        return c

    def toplama(*args):
        sum = 0
        for i in args:
            sum += i
        return sum
    if islemadi == "Toplama":
        return toplama
    elif islemadi == "Çarpma":
        return carpma
    else:
        print("gecersiz islem adı...")


fun1 = anafonksiyon("Toplama")
fun2 = anafonksiyon("Çarpma")
print(fun1(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
print(fun2(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

# fonksiyon paremetre gondermek


def anaafonksiyon(fun1, fun2, fun3, fun4, islemadi):
    if islemadi == "T":
        print(fun1(4, 3))
    elif islemadi == "C":
        print(fun2(4, 3))
    elif islemadi == "car":
        print(fun3(4, 3))
    elif islemadi == "b":
        print(fun4(4, 3))


def toplam(a, b):
    return a+b


def cıkarma(a, b):
    return a-b


def carpmak(a, b):
    return a*b


def bolme(a, b):
    return a/b


anaafonksiyon(toplam, cıkarma, carpmak, bolme, "car")
