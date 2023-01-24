# try except
"""
try:
    hata oluşabilecek kodlar
except:#hata yazılmassa bütün hatalar bu bloğa düşer
    hata varsa buraya düşer     
    """
try:
    int("jjs77")  # hata aldı except bloğuna düştü
    print("kod burada")
except ValueError:
    print("sayı giriniz...")
try:
    int("77")  # hata almadı except bloğuna düşmedi
    print("kod burada")
except ValueError:
    print("sayı giriniz...")
try:
    a = int(input("a:"))
    b = int(input("b:"))
    print(a/b)
    print("kod burada")
except ValueError:
    print("sayı giriniz...")
except ZeroDivisionError:
    print("bir sayı 0 a bolunemez")
try:
    c = int(input("c:"))
    d = int(input("d:"))
    print(c/d)
    print("kod burada")
except (ValueError, ZeroDivisionError):
    print("sayı giriniz... veya sıfıra bolmeyiniz")
finally:
    print("kod burada...")  # finally ne olursa olsun çalışacak kod
# raise hata fırlatmak


def ters_çevir(metin):
    if type(metin) != str:
        raise ValueError("metin giriniz...")
    else:
        print(metin[::-1])


ters_çevir("skjs")
ters_çevir(444)
