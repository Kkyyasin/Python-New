class Calisan():
    def __init__(self, isim, maas, departman):
        print("Calisan__init() called")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def __str__(self):
        return """
            Calisan Bilgileri
    
    Ad :{}
    Maas :{}
    Departman :{}
        """.format(self.isim, self.maas, self.departman)


class Yonetici(Calisan):  # Calısandaki bilgiler alınır
   # __init__() ustteki calisir
    def departman_değiştir(self, yeni_departman):
        self.departman = yeni_departman

    def maas_zam_yap(self, miktar):
        self.maas += miktar


class Yonetici2(Calisan):  # Calısandaki bilgiler alınır
    # çalışan objesinde __init__ metedunu iptal etti.
    def __init__(self, isim, maas, departman, kisi_sayısı):
        print("Yönetici initi çalıştı")
        self.isim = isim
        self.maas = maas
        self.departman = departman
        self.kisi_sayısı = kisi_sayısı

    def departman_değiştir(self, yeni_departman):
        self.departman = yeni_departman

    def bilgileri_göster(self):
        print("Çalışan Bilgileri\n")
        print("Ad:{}\nDepartman:{}\nMaaş:{}\nSorumlu olduğu kişi sayısı:{}\n".format(
            self.isim, self.departman, self.maas, self.kisi_sayısı))

    def maas_zam_yap(self, miktar):
        self.maas += miktar


class Yonetici3(Calisan):
    def __init__(self, isim, maas, departman, kisi_sayısı):
        # super metodu yukardaki metdu çalıştırmayı sağlar
        super().__init__(isim, maas, departman)
        print("Yönetici initi çalıştı")
        self.kisi_sayısı = kisi_sayısı  # iki initide çalıştırır

    def departman_değiştir(self, yeni_departman):
        self.departman = yeni_departman

    def bilgileri_göster(self):
        print("Çalışan Bilgileri\n")
        print("Ad:{}\nDepartman:{}\nMaaş:{}\nSorumlu olduğu kişi sayısı:{}\n".format(
            self.isim, self.departman, self.maas, self.kisi_sayısı))

    def maas_zam_yap(self, miktar):
        self.maas += miktar


yönetici = Yonetici("Ahmet", 5000, "İnsan Kaynakları")
print(yönetici.__str__())
yönetici.departman_değiştir("Bilişim")
yönetici.maas_zam_yap(500)
print(yönetici.__str__())
yönetici3 = Yonetici3("Mehmet", 5000, "Genel Müdür", 100)
yönetici3.bilgileri_göster()
yönetici2 = Yonetici2("Mehmet", 5000, "Genel Müdür", 100)
yönetici2.bilgileri_göster()
