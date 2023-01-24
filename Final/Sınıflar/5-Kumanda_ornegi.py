import random


class Kumanda():
    def __init__(self, ad="Bilinmiyor", tv_durum="Kapali", kanallar=["Trt", "Start"], ses=80, su_anki_kanal="Trt"):
        self.tv_durum = tv_durum
        self.kanallar = kanallar
        self.su_anki_kanal = su_anki_kanal
        self.ses = ses
        self.ad = ad

    def __str__(self):
        return """
                {0}
    TV Durum : {1}
    Oynatilan Kanal :{2}
    Ses : {3}
    Kanallar : {4}    
        """.format(self.ad, self.tv_durum, self.su_anki_kanal, self.ses, self.kanallar)

    def __len__(self):
        return len(self.kanallar)

    def __eq__(self, other):
        if isinstance(other, Kumanda):
            return other.ad == self.ad
        return False

    def Ac(self):
        print("Televizyon aciliyor...")
        self.tv_durum = "Acik"

    def Kapat(self):
        print("Televizyon kapaniyor")
        self.tv_durum = "Kapali"

    def SesArttir(self):
        if (self.ses+1) <= 100:
            self.ses += 1
        print("Ses :"+str(self.ses))

    def SesAzalt(self):
        if (self.ses-1) >= 0:
            self -= 1
        print("Ses :"+str(self.ses))

    def KanalEkle(self):
        ekle = input("Eklemek istediginiz kanali giriniz:")
        self.kanallar.append(ekle)

    def KanalSil(self):
        self.KanalGoster()
        sil = input("Silmek istediginiz kanali giriniz:")
        self.kanallar.remove(sil)
        print("Kanal silindi...")

    def KanalGoster(self):
        for i in self.kanallar:
            print((self.kanallar.index(i)+1), "-", i)

    def KanalDegistir(self):
        self.KanalGoster()
        try:
            degisim = int(
                input("Degistirmek istediginiz kanalin numarasini giriniz:"))
            if degisim < 0 or degisim > len(self.kanallar):
                raise IndexError("Lütfen dogru aralik giriniz...")
            self.su_anki_kanal = self.kanallar[degisim-1]
        except ValueError:
            print("Lutfen sayi giriniz...")
        except IndexError:
            print(IndexError)

    def RasgeleKanal(self):
        self.su_anki_kanal = random.choice(self.kanallar)


Samsung_Tv = Kumanda("Samsung Tv")
while True:
    secim = input("""
    Televizyon Uygulaması
    
1-Tv aç

2-Tv kapat

3-Ses Arttir

4-Ses Azalt

5-Kanal ekle

6-Kanal sil

7-Kanallari Goster

8-Kanal sayısı öğrenme

9-Kanal değiştir

10-Rastgele kanal

11-Televizyon Bilgileri


Çıkmak için 'q' ya basın.

secim:""")
    if secim == "1":
        Samsung_Tv.Ac()
    elif secim == "2":
        Samsung_Tv.Kapat()
    elif secim == "3":
        Samsung_Tv.SesArttir()
    elif secim == "4":
        Samsung_Tv.SesAzalt()
    elif secim == "5":
        Samsung_Tv.KanalEkle()
    elif secim == "6":
        Samsung_Tv.KanalSil()
    elif secim == "7":
        Samsung_Tv.KanalGoster()
    elif secim == "8":
        print("Kanal sayısı:", len(Samsung_Tv))
    elif secim == "9":
        Samsung_Tv.KanalDegistir()
    elif secim == "10":
        Samsung_Tv.RasgeleKanal()
    elif secim == "11":
        print(Samsung_Tv)
    elif secim == "q":
        print("Çıkış Yapılıyor...")
        break
    else:
        print("Hatakı kodlama...")
