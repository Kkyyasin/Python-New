"""Siz de bir tane Şarkı projesi geliştirmeye çalışın.

                     Örnek özellikler;

                     1. Şarkı İsmi
                     2. Sanatçı
                     3. Albüm
                     4. Prodüksiyon Şirketi
                     5. Şarkı Süresi

                     Örnek Metodlar;

                     1. Veritabanındaki Toplam Şarkı Süresini Hesaplayan Metod
                     2. Şarkı Ekle
                     3. Şarkı Sil"""
import sqlite3
import time

import random


class Sarkı():

    def __init__(self, isim="Bilinmiyor", sanatci="Bilinmeyen", albüm="Bilgi yok", produceksiyon="Bilgi yok", sure=0):
        self.isim = isim
        self.sanatci = sanatci
        self.albüm = albüm
        self.produceksiyon = produceksiyon
        self.sure = sure

    def __str__(self):
        return """
    Şarkı ismi:{}
    Sanatçı:{}
    Albüm:{}
    Prodüksiyon Şirketi:{}
    Şarkı süresi:{}
    """.format(self.isim, self.sanatci, self.albüm, self.produceksiyon, self.sure)

    def __len__(self):
        return self.sure


class Mp3calar():
    def __init__(self):
        self.baglantı_olustur()
        self.dosya_baglantı_olustur()

        self.suancalansarki = ""
        self.ses = 100
        self.durum = True
        self.veri_tabanı_text()

    def baglantı_olustur(self):
        self.baglantı = sqlite3.connect("Sarkı_Listesi.db")
        self.imlec = self.baglantı.cursor()
        self.imlec.execute(
            "CREATE TABLE IF NOT EXISTS Sarkı_Listesi(Şarkı_İsmi TEXT,Sanatcı_İsmi TEXT,Albüm TEXT,Prodüksiyon TEXT,Sure INT)")
        self.baglantı.commit()

    def dosya_baglantı_olustur(self):
        try:
            with open("Sarkı_Listesi.txt", "r", encoding="utf-8") as file:
                self.file_liste = file.readlines()
        except FileNotFoundError:
            with open("Sarkı_Listesi.txt", "w", encoding="utf-8") as file:
                file.write("\t\t-------------Şarkı Listesi---------\n\n")

    def sarkı_ekle(self, s=Sarkı()):
        # sqlite ekleme
        self.imlec.execute("INSERT INTO Sarkı_Listesi Values(?,?,?,?,?)",
                           (s.isim, s.sanatci, s.albüm, s.produceksiyon, s.sure))
        self.baglantı.commit()
        # txt ekleme
        with open("Sarkı_Listesi.txt", "a+", encoding="utf-8") as file:
            indix = len(self.file_liste)-1
            file.write("{}-{}\t\t{}\t{}\t{}\t{}\n".format(indix,
                       s.isim, s.sanatci, s.albüm, s.produceksiyon, s.sure))

    def sarkı_sil(self):
        # sqlite silme
        self.sarkı_listesi()
        isim = input("Silmek istediğiniz şarkı ismini giriniz:")
        with open("Sarkı_Listesi.txt", "r", encoding="utf-8") as file:
            a = file.readlines()
            b = a[2:]
            for j, i in enumerate(b):
                i = i.split("-")

                i = i[1].split()

                if i[0] == isim:
                    a.pop(j+2)
                    c = 1
                    break
        with open("Sarkı_Listesi.txt", "w", encoding="utf-8") as file:
            file.write("\t\t-------------Şarkı Listesi---------\n\n")
            for i, j in enumerate(a):
                if i < 2:
                    pass

                else:
                    j = j.split("-")
                    j = j[1].split()
                    print(j)
                    file.write("{}-{}\t\t{}\t{}\t{}\t{}\n".format(i-1,
                                                                  j[0], j[1], j[2], j[3], j[4]))

        if c == 1:
            self.imlec.execute(
                "DELETE FROM Sarkı_Listesi WHERE Şarkı_İsmi=?", (isim,))
            self.baglantı.commit()
        else:
            print("Sarkı yoktur...")

    def sarkı_degistir(self):
        while True:
            secim = input("0-Çıkış\n1-Rastgele secim\n2-Manuel secim\nsecim:")
            c = 0
            if secim == "0":
                break
            elif secim == "1":
                self.rasgele_sarkı_sec()
                break
            elif secim == "2":
                self.sarkı_listesi()
                self.imlec.execute("SELECT * FROM Sarkı_Listesi")
                liste = self.imlec.fetchall()
                while True:
                    isim = input("Şarkı ismini giriniz:")

                    for i in liste:
                        if i[0] == isim:
                            c = 1
                            s = Sarkı(*i)
                            self.suancalansarki = s
                            print("Suan Çalan sarkı:", s)
                            break
                    if c == 1:
                        break
                    elif isim == "0":
                        break
                    else:
                        print("Sarkı bulunmuyor çıkmak için sıfıra tuslayın")
                break

    def veri_tabanı_text(self):
        self.imlec.execute("SELECT * FROM Sarkı_Listesi")
        liste = self.imlec.fetchall()

        with open("Sarkı_Listesi.txt", "w", encoding="utf-8") as file:
            file.write("\t\t-------------Şarkı Listesi---------\n\n")
            for i, j in enumerate(liste):

                print(file.tell())
                file.write("{}-{}\t\t{}\t{}\t{}\t{}\n".format(i+1,
                                                              j[0], j[1], j[2], j[3], j[4]))

    def rasgele_sarkı_sec(self):
        self.imlec.execute("SELECT * FROM Sarkı_Listesi")
        liste = self.imlec.fetchall()
        rasgele = random.choice(liste)
        s = Sarkı(*rasgele)
        self.suancalansarki = s
        print("Suan Çalan sarkı:", s)

    def ses_degistir(self):
        while True:
            secim = input("\n\n0-Çıkıs\n1-Ses Arttır\n2-Ses Azalt\nsecim:")
            if secim == "0":
                break
            elif secim == "1":
                if (self.ses+1) != 101:
                    self.ses += 1
                print("Ses:{}".format(self.ses))
            elif secim == "2":
                if (self.ses-1) != -1:
                    self.ses -= 1
                    print("Ses:{}".format(self.ses))
            else:
                print("Ses:{}".format(self.ses))

    def sarkı_listesi(self):
        self.imlec.execute("SELECT * FROM Sarkı_Listesi")
        liste = self.imlec.fetchall()
        for i, j in enumerate(liste):
            a = Sarkı(*j)
            print(i+1, "-", a)

    def Toplam_sarkı_suresi(self):
        self.imlec.execute("SELECT Sure FROM Sarkı_Listesi")
        liste = self.imlec.fetchall()
        return sum(liste)

    def baglantı_kes(self):
        self.baglantı.close()


mp3 = Mp3calar()
while mp3.durum:
    secim = input("""

    \t\t|************************************************************|
    \t\t|---------------------------Mp3calar-------------------------|
    \t\t|____________________________________________________________|


    \t0-Çıkış
    \t1-Şarkı Ekle
    \t2-Şarkıları Göster
    \t3-Şarkı Sil
    \t4-Şarkı değiştir
    \t5-Ses değistir

    secim:""")
    if secim == "0":
        mp3.baglantı_kes()
        mp3.durum = False
    elif secim == "1":
        isim = input("Şarkı ismi:")
        Sanatcı = input("Sanatcı:")
        Albüm = input("Albüm:")
        prodiksiyon = input("Prodiksiyon:")
        sure = float(input("sure:"))
        mp3.sarkı_ekle(Sarkı(isim, Sanatcı, Albüm, prodiksiyon, sure))
    elif secim == "2":
        mp3.sarkı_listesi()
    elif secim == "3":
        mp3.sarkı_sil()
    elif secim == "4":
        mp3.sarkı_degistir()
    elif secim == "5":
        mp3.ses_degistir()
    else:
        print("Hatalı kodlama...")
