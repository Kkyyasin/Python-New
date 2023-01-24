from tkinter import Y


class Çalışan():
    def __init__(self, isim, maas, departman):
        print("Çalışan initi çalıştı")
        self.isim = isim
        self.maas = maas
        self.departman = departman

    def bilgileri_göster(self):
        print("Çalışan Bilgileri\n")
        print("Ad:{}\nDepartman:{}\nMaaş:{}\n".format(
            self.isim, self.departman, self.maas))


class Yönetici(Çalışan):  # çalışandaki bilgileri alır

    def departman_değiştir(self, yeni_departman):
        self.departman = yeni_departman

    def maas_zam_yap(self, miktar):
        self.maas += miktar


print("\n***********************************************************************************************\n")

yönetici = Yönetici("Ahmet", 5000, "İnsan Kaynakları")
yönetici.bilgileri_göster()
yönetici.departman_değiştir("Bilişim")
yönetici.maas_zam_yap(500)
yönetici.bilgileri_göster()
# Overriding (İptal etme) bilgilerini aldığımız objeden tekrar metod tanımlayarak diğer metdo iptal olur


class Yönetici2(Çalışan):
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


print("\n***********************************************************************************************\n")

yönetici2 = Yönetici2("Mehmet", 5000, "Genel Müdür", 100)
yönetici2.bilgileri_göster()
# super metodu


class Yönetici3(Çalışan):
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


print("\n***********************************************************************************************\n")
yönetici3 = Yönetici3("Mehmet", 5000, "Genel Müdür", 100)
yönetici3.bilgileri_göster()
