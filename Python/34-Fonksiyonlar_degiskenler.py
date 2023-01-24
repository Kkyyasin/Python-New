# Global değişken
a = 5


def fonksiyon():
    print(a)


fonksiyon()

"""
def fonksiyon2():
    print(b)
#burda hata alır global değşken önce tanımlanmalı

fonksiyon2()
b = 2"""
# yerel değişken


def fonksiyon3():
    c = 2
    print(c)


fonksiyon3()
# karışık
c = 2


def fonksiyon4():
    c = 4
    print(c)  # yerel değişken


print(c)  # global değişken
fonksiyon4()
# global deyimi fonksiyon içinde değerini değiştirmeye yarar
d = 5


def fonksiyon5():
    global d
    d = 3
    print(d)


fonksiyon5()
print(d)
