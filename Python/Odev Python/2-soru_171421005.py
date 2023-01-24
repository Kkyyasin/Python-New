import pickle

"""
Muhammed Yasin Özdemir
171421005
"""


class Araba():
    def __init__(self, marka="Yok", model="Yok", renk="Yok", fiyat=0, hiz=0):
        self.marka = marka
        self.model = model
        self.renk = renk
        self.fiyat = fiyat
        self.hiz = hiz

    def __str__(self):
        return """
    MARKA    :{}
    MODEL    :{}
    RENK     :{}
    FIYAT    :{}
    HIZ      :{}
    """.format(self.marka, self.model, self.renk, self.fiyat, self.hiz)


class Program():
    def __init__(self):
        self.DosyaOku()
        self.durum = True

    def Menu(self):
        return """
    \t\t******************** Menu ********************
    
            0-Çıkış
            1-Araç Ekle
            2-Araçları göster
            3-Araç Sil
            4-Araç Guncelle
            
    secim(0-4):"""

    def Calis(self):
        while self.durum:
            secim = input(self.Menu())
            if secim == "0":
                self.durum = False
            elif secim == "1":
                self.Ekle()
            elif secim == "2":
                self.Goster()
            elif secim == "3":
                self.Sil()
            elif secim == "4":
                self.Guncelle()
            else:
                print("Lütfen doğru seçim yapınız...")

    def Goster(self):
        for araba in self.arabalar:
            print("\n{}-{}".format(self.arabalar.index(araba)+1, araba))

    def Ekle(self):
        marka = input("Marka :")

        model = input("Model :")
        renk = input("Renk :")
        if marka.strip() == "":
            marka = None
        while True:
            try:
                fiyat = float(input("Fiyat :"))
                hiz = float(input("Hiz :"))
                break
            except:
                print("Lütfen sayı giriniz")
        self.arabalar += [Araba(marka=marka, model=model,
                                renk=renk, fiyat=fiyat, hiz=hiz)]
        self.DosyaGuncelle()
        print("\nAraba başarıyla eklendi...\n")

    def Sil(self):
        self.Goster()
        while True:
            try:
                indis = int(
                    input("Silmek istediğiniz arabasının numarasını giriniz :"))-1
                if(indis < 0 and indis > len(self.arabalar)):
                    print("Lütfen aralığı doğru giriniz")
                    continue
                break
            except:
                print("Lütfen sayı giriniz")
        self.arabalar.remove(self.arabalar[indis])
        self.DosyaGuncelle()
        print("\nAraba başarıyla silindi...\n")

    def Guncelle(self):
        self.Goster()
        while True:
            try:
                indis = int(
                    input("Güncellemek istediğiniz arabasının numarasını giriniz :"))-1
                if(indis < 0 and indis > len(self.arabalar)):
                    print("Lütfen aralığı doğru giriniz")
                    continue
                break
            except:
                print("Lütfen sayı giriniz")
        araba = self.arabalar[indis]
        while True:
            gsec = input("""
            0.Çıkış
            1-Marka Guncelle
            2-Model Guncelle
            3-Renk Guncelle
            4-Fiyat Güncelle
            5-Hız Güncelle
        
        secim :""")
            if gsec == "0":
                break
            elif gsec == "1":
                print("Eski Marka :", araba.marka)
                marka = input("Marka :")
                araba.marka = marka
                print("Marka güncellendi...")
            elif gsec == "2":
                print("Eski Model :", araba.model)
                model = input("Model :")
                araba.model = model
                print("Model güncellendi...")
            elif gsec == "3":
                print("Eski Renk :", araba.renk)
                renk = input("Renk :")
                araba.renk = renk
                print("Renk güncellendi...")
            elif gsec == "4":
                while True:
                    try:
                        print("Eski Fiyat :", araba.fiyat)
                        fiyat = float(input("Fiyat :"))
                        araba.fiyat = fiyat
                        print("Fiyat güncellendi...")
                        break
                    except:
                        print("Lütfen sayı giriniz")
            elif gsec == "5":
                while True:
                    try:
                        print("Eski Hız :", araba.hiz)
                        hiz = float(input("Hiz :"))
                        araba.hiz = hiz
                        print("Hız güncellendi...")
                        break
                    except:
                        print("Lütfen sayı giriniz")
            else:
                print("Hatalı secim...")

        self.arabalar[indis] = araba
        self.DosyaGuncelle()
        print("\nAraba başarıyla güncellendi...\n\n{}".format(araba))

    def DosyaGuncelle(self):
        with open("arabalar.pkl", "wb") as dosya:
            pickle.dump(self.arabalar, dosya)

    def DosyaOku(self):
        try:
            with open("arabalar.pkl", "rb") as dosya:
                self.arabalar = pickle.load(dosya)
        except:
            self.arabalar = list()


program = Program()
program.Calis()
print("\nProgram sonlandı...")
