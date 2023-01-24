import sqlite3
con = sqlite3.connect("Kutuphane.db")
cursor = con.cursor()


def veri_guncelle():
    cursor.execute(
        "Update Kutuphane set Sayfa=100 where Sayfa=5")
    con.commit()


def veri_al():
    cursor.execute("SELECT * FROM Kutuphane")
    liste = cursor.fetchall()
    for i in liste:
        print(i)


def veri_sile():
    cursor.execute("DELETE FROM Kutuphane WHERE İsim='ww'")  # isim ww silinir
    con.commit()


veri_al()
veri_guncelle()
veri_al()
veri_sile()
veri_al()
