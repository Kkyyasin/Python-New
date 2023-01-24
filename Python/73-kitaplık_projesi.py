import sqlite3
import time


class Kitap():
    def __init__(self, İsim, Yazar, Sayfa_Sayısı, Baskı, Tur):
        self.İsim = İsim
        self.Yazar = Yazar
        self.Sayfa_Sayısı = Sayfa_Sayısı
        self.Baskı = Baskı
        self.Tur = Tur

    def __str__(self):
        return """
    Kitap Adı:{}
    Yazar:{}
    Sayfa Sayısı:{}
    Baskı:{}
    Tür:{}
    """.format(self.İsim, self.Yazar, self.Sayfa_Sayısı, self.Baskı, self.Tur)

    def __len__(self):
        return self.Sayfa_Sayısı


class Kitaplık():

    def __init__(self):
        self.baglanti_olustur()

    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("Kitaplık.db")
        self.imlec = self.baglanti.cursor()
        try:
            self.imlec.execute(
                "CREATE TABLE IF NOT EXISTS Kitaplık(Kitap_Adı TEXT,Yazar TEXT,Sayfa_Sayısı INT,Baskı INT,Tür TEXT)")
        except sqlite3.OperationalError:
            print("ww")
        self.baglanti.commit()
        self.kitap = Kitap()

    def kitapları_goster(self):
        self.imlec.execute("SELECT * FROM Kitaplık")
        liste = self.imlec.fetchall()
        for i, j in enumerate(liste):
            kitap = Kitap(j[0], j[1], j[2], j[3], j[4])
            print(i+1, "-", kitap)

    def kitap_bul(self):
        isim = input("Kitap ismi giriniz:")
        self.imlec.execute(
            "SELECT * FROM Kitaplık where Kitap_Adı=?", (isim,))
        liste = self.imlec.fetchall()
        if len(liste) == 0:
            print("Kitap yoktur...")
        else:
            kitap = Kitap(liste[0][0], liste[0][1], liste[0]
                          [2], liste[0][3], liste[0][4])
            print(kitap)

    def kitap_ekle(self):
        isim = input("Kitap Adı:")
        Yazar = input("Yazar:")
        while True:
            try:
                sy_sayısı = int(input("Sayfa sayısı:"))
                baskı = input("Baskı:")
                break
            except ValueError:
                print("lutfen sayi giriniz")
        tur = input("Tür:")
        self.imlec.execute("INSERT INTO Kitaplık Values(?,?,?,?,?)",
                           (isim, Yazar, sy_sayısı, baskı, tur))
        self.baglanti.commit()
        print("kitap eklendi...")

    def kitap_sil(self):
        self.kitapları_goster()
        isim = input("Kitap Adı:")
        self.imlec.execute("Delete from Kitaplık where Kitap_Adı=?", (isim,))
        self.baglanti.commit()
        print("Kitap silindi...")

    def baskı_yükselt(self):
        self.kitapları_goster()
        ad = input("Yükselt istediğiniz kitap adı giriniz:")
        self.imlec.execute("Select Baskı from where Kitap_Adı=?", (ad))
        a = self.imlec.fetchall()
        if (len(a) == 0):
            print("kitap yok...")
        else:
            a[0] += 1
        self.imlec.execute(
            "Update Kitaplık set Baskı=? Kitap_Adı=?", (a[0], ad))
        self.baglanti.commit()

    def baglantı_kes(self):
        self.baglanti.close()


kitaplık = Kitaplık()
while True:
    secim = input("""
        0-Çıkış
        1-Kitap ekle
        2-Kitap Sil
        3-Kitapları göster
        4-Kitap bul
        5-Baskı Yükselt
                """)
    if secim == "0":
        kitaplık.baglantı_kes()
        break
    elif secim == "1":
        kitaplık.kitap_ekle()
    elif secim == "2":
        kitaplık.kitap_sil()
    elif secim == "3":
        kitaplık.kitapları_goster()
    elif secim == "4":
        kitaplık.kitap_bul()
    elif secim == "5":
        kitaplık.baskı_yükselt()
    else:
        print("Hatalı kodlama...")
