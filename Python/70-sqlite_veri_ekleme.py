import sqlite3

from numpy import isin

con = sqlite3.connect("Kutuphane.db")
cursor = con.cursor()


def tablo_eleman_ekle():
    isim = input("Isim: ")
    Yazar = input("Yazar:")
    sayfa_sayısı = int(input("Sayfa: "))
    cursor.execute("INSERT INTO Kutuphane Values('{}','{}',{})".format(
        isim, Yazar, sayfa_sayısı))  # ınsert into falan buyuk veya kucuk yazılabilirama genelde buyuk yazılır
    con.commit()


def tablo_eleman_ekle2():
    isim = input("Isim: ")
    Yazar = input("Yazar:")
    sayfa_sayısı = int(input("Sayfa: "))
    # ınsert into falan buyuk veya kucuk yazılabilirama genelde buyuk yazılır
    cursor.execute("INSERT INTO Kutuphane Values(?,?,?)",
                   (isim, Yazar, sayfa_sayısı))
    con.commit()


tablo_eleman_ekle()
tablo_eleman_ekle2()
con.close()
