from operator import index
import time
import random


class Kumanda():
    def __init__(self, tv_durum="Kapalı", Ses=100, kanal_listesi=["Trt", "Star tv"], suanki_kanal="Trt"):
        self.tv_durum = tv_durum
        self.suanki_kanal = suanki_kanal
        self.Ses = Ses
        self.kanal_listesi = kanal_listesi

    def tv_ac(self):
        if self.tv_durum == "Kapalı":
            print("Tv açılıyor...")
            self.tv_durum = "Açık"
        else:
            print("Tv zaten açık...")

    def tv_kapat(self):
        if self.tv_durum == "Açık":
            print("Tv Kapanıyor...")
            self.tv_durum = "Kapalı"
        else:
            print("Tv zaten Kapalı...")

    def ses_durum(self):
        print("1-Ses arttır:+\n2-Ses azalt:-\n3-Çıkış:herhangi bir tuş")
        while True:
            cevap = input("cevap:")
            if cevap == "+":
                if self.Ses == 100:
                    print("Ses:{}".format(self.Ses))
                else:
                    self.Ses += 1
                    print("Ses:{}".format(self.Ses))
            elif cevap == "-":
                if self.Ses == 0:
                    print("Ses:{}".format(self.Ses))
                else:
                    self.Ses -= 1
                    print("Ses:{}".format(self.Ses))
            else:
                break

    def kanal_ekle(self, kanal_ismi):
        print("kanal ekleniyor...")
        time.sleep(1)
        self.kanal_listesi.append(kanal_ismi)
        print("kanal eklendi")

    def kanal_sil(self):
        for i in range(len(self.kanal_listesi)):
            print(i+1, "-", self.kanal_listesi[i])
        while True:
            try:
                secim = int(input("Kanal seciniz:"))
                secim -= 1
                if self.kanal_listesi[secim] == None:
                    continue
                else:
                    print("kanal siliniyor...")
                    time.sleep(1)
                    self.kanal_listesi.pop(secim)
                    print("kanal silindi")
                    break
            except ValueError:
                print("Lütfen gecerli sayı giriniz...")

    def rasgele_kanal(self):
        self.suanki_kanal = random.choice(self.kanal_listesi)

    def kanal_değiştir(self):
        for i in range(len(self.kanal_listesi)):
            print(i+1, "-", self.kanal_listesi[i])
        while True:
            try:
                secim = int(input("Kanal seciniz:"))
                secim -= 1
                if self.kanal_listesi[secim] == None:
                    continue
                else:
                    self.suanki_kanal = self.kanal_listesi[secim]
                    break
            except ValueError:
                print("Lütfen gecerli sayı giriniz...")

    def __str__(self):
        return "Tv Durumu:{}\nKanal listesi:{}\nŞuanki Kanal: {}\nSes:{}".format(self.tv_durum, self.kanal_listesi, self.suanki_kanal, self.Ses)

    def __len__(self):
        return len(self.kanal_listesi)


Samsung_Tv = Kumanda()
while True:
    secim = input("""
    Televizyon Uygulaması
    
1-Tv aç

2-Tv kapat

3-Ses Ayarları

4-Kanal ekle

5-Kanal sil

6-Kanal sayısı öğrenme

7-Kanal değiştir

8-Rastgele kanal

9-Televizyon Bilgileri


Çıkmak için 'q' ya basın.

secim:""")
    if secim == "1":
        Samsung_Tv.tv_ac()
    elif secim == "2":
        Samsung_Tv.tv_kapat()
    elif secim == "3":
        Samsung_Tv.ses_durum()
    elif secim == "4":
        kanal = input("Eklemek istediğiniz kanalı giriniz:")
        Samsung_Tv.kanal_ekle(kanal)
    elif secim == "5":
        Samsung_Tv.kanal_sil()
    elif secim == "6":
        print("Kanal sayısı:", len(Samsung_Tv))
    elif secim == "7":
        Samsung_Tv.kanal_değiştir()
    elif secim == "8":
        Samsung_Tv.rasgele_kanal()
    elif secim == "9":
        print(Samsung_Tv)
    elif secim == "q":
        print("Çıkış Yapılıyor...")
        break
    else:
        print("Hatakı kodlama...")
