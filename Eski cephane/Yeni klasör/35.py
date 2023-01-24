from sqlite3 import *
with connect("veri tabani1.db") as baglanti:
    imlec=baglanti.cursor()
    imlec.execute("SELECT İsim ,Yas,Cinsiyet from uyeler")

    for isim,yas,cinsiyet in imlec.fetchall():
        print("""
    isim:{}
    yas:{}
    cinsiyet:{}
        """.format(isim,cinsiyet,yas))
    baglanti.commit()
with connect("veri tabani1.db") as baglanti:
    imlec=baglanti.cursor()
    imlec.execute("SELECT İsim  from uyeler")

    for isim in imlec.fetchall():
        print("""
    isim:{}
  
        """.format(isim[0]))
    baglanti.commit()
with connect("veri tabani1.db") as baglanti:
    imlec=baglanti.cursor()
    imlec.execute("SELECT * from uyeler WHERE Yas<18")

    for isim,yas,cinsiyet in imlec.fetchall():
        print("""
    isim:{}
    yas:{}
    cinsiyet:{}
        """.format(isim,cinsiyet,yas))
    baglanti.commit()
with connect("veri tabani1.db") as baglanti:
    imlec=baglanti.cursor()
    imlec.execute("UPDATE uyeler SET Yas=21 WHERE İsim =='zeynep'")
    imlec.execute("SELECT * from uyeler")
    for isim,yas,cinsiyet in imlec.fetchall():
        print("""
    isim:{}
    yas:{}
    cinsiyet:{}
        """.format(isim,cinsiyet,yas))
    baglanti.commit()
with connect("veri tabani1.db") as baglanti:
    imlec=baglanti.cursor()
    imlec.execute("DELETE from uyeler WHERE İsim=='selin'")
    imlec.execute("SELECT * from uyeler")
    for isim,yas,cinsiyet in imlec.fetchall():
        print("""
    isim:{}
    yas:{}
    cinsiyet:{}
        """.format(isim,cinsiyet,yas))
    baglanti.commit()




