class Yazilimci():
    def __init__(self, ad, soyad, yas):
        self.ad = ad
        self.soyad = soyad
        self.bildigi_diller = []
        self.yas = yas

    def __str__(self):
        return "Ad:{}\nSoyad:{}\nYas:{}\nBildigi Diller:{}".format(self.ad, self.soyad, self.yas, self.bildigi_diller)

    def DilEkle(self):
        ekle = input("Eklemek istediginiz dili giriniz:")
        self.bildigi_diller.append(ekle)
        print("Dil eklendi...")

    def DilGoster(self):
        for i in self.bildigi_diller:
            print(i)

    def DilSİl(self):
        self.DilGoster()
        sil = input("dil seciniz:")
        self.Bildigi_diller.remove(sil)

    def Menu(self):
        while(True):
            sec = input("""
            1-Dil Ekle
            2-Dilleri Goster
            3-Dil Sil
            4-Çıkıs
    secim: """)
            if sec == "1":
                self.DilEkle()
            elif sec == "2":
                self.DilGoster()
            elif sec == "3":
                self.DilSİl()
            elif sec == "4":
                break
            else:
                print("Hatali kodlama...")


yazilimcilar = []
while True:
    sec = input("""
        1-Yazılımcı ekle
        2-Yazılımcı Sil
        3-Yazlımcıları göster
        4-Çıkış
   secim:""")
    if sec == "1":
        ad = input("ad:")
        soyad = input("soyad:")
        yas = input("yas:")
        newsoftware = Yazilimci(ad, soyad, yas)
        yazilimcilar.append(newsoftware)
    elif sec == "2":
        for i in range(len(yazilimcilar)):
            print(str(i+1) + "-" + yazilimcilar[i].__str__())
        try:
            secim = int(input("silmek istediginiz kisinin numarasini giriniz"))
        except ValueError:
            print("Lütfen sayı girimiz")
        yazilimcilar.pop(secim-1)
    elif sec == "3":

        for i in range(len(yazilimcilar)):
            print(str(i+1) + "-" + yazilimcilar[i].__str__())
    elif sec == "4":
        break
    else:
        print("Hatali kodlama...")
