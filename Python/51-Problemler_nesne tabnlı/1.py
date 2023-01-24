"""Bir tane "Bilgisayar" sınıfı oluşturarak bu sınıfa metodlar ve özellikler ekleyin ve bu class'ı kullanmaya çalışın.

Bu sınıfı yazarken öğrendiğimiz özel metodların hepsini tanımlamaya çalışın.
    """


class Bilgisayar():
    def __init__(self, pc=[{"marka": "monster", "işlemci": "intel i7", "ekran kartı": "nvidia 3050ti", "ram": 16, "ssd": 512, "fiyat": 12000}]):
        self.pc = pc

    def bilgisayarları_göster(self):
        c = 1
        for i in self.pc:
            print("\n", c, "-", i["marka"], "\n")
            for k, l in i.items():
                print("\t", "{}:{}".format(k, l))
            c += 1

    def bilgisayar_ekle(self, marka, işlemci, ekran_kartı, ram, ssd, fiyat):
        self.pc.append({"marka": marka, "işlemci": işlemci,
                       "ekran kartı": ekran_kartı, "ram": ram, "ssd": ssd, "fiyat": fiyat})
        print("Bilgisayar yüklendi...")

    def bilgisayar_çıkar(self):
        self.bilgisayarları_göster()
        while True:
            try:
                secim = int(
                    input("Çıkarmak istediğiniz markanın numarısını giriniz:"))
                secim -= 1
                if secim >= 0 and secim < len(self.pc) and len(self.pc) != 0:
                    self.pc.pop(secim)
                    print("Bilgisayar başarıyla silindi...")
                    break
                else:
                    print("lütfen doğru sayıyı giriniz...")
            except ValueError:
                print("Sayı giriniz...")

    def fiyat_değiştir(self):
        self.bilgisayarları_göster()
        while True:
            try:
                secim = int(
                    input("Fiyatını değiştirmek  istediğiniz markanın numarısını giriniz:"))
                secim -= 1
                if secim >= 0 and secim < len(self.pc) and len(self.pc) != 0:
                    fiyat = float(
                        input("Eski fiyat:{}\nYeni fiyat giriniz:".format(self.pc[secim]["fiyat"])))
                    self.pc[secim]["fiyat"] = fiyat
                    print("Fiyat başarıyla değiştirildi...")
                    break
                else:
                    print("lütfen doğru sayıyı giriniz...")
            except ValueError:
                print("Sayı giriniz...")

    def ram_değiştir(self):
        self.bilgisayarları_göster()
        while True:
            try:
                secim = int(
                    input("Ram değiştirmek  istediğiniz markanın numarısını giriniz:"))
                secim -= 1
                if secim >= 0 and secim < len(self.pc) and len(self.pc) != 0:
                    ram = float(
                        input("Eski ram:{}\nYeni ram giriniz:".format(self.pc[secim]["ram"])))
                    self.pc[secim]["ram"] = ram
                    print("Ram başarıyla değiştirldi...")
                    break
                else:
                    print("lütfen doğru sayıyı giriniz...")
            except ValueError:
                print("Sayı giriniz...")

    def ssd_değiştir(self):
        self.bilgisayarları_göster()
        while True:
            try:
                secim = int(
                    input("Ssd değiştirmek  istediğiniz markanın numarısını giriniz:"))
                secim -= 1
                if secim >= 0 and secim < len(self.pc) and len(self.pc) != 0:
                    ssd = float(
                        input("Eski ssd:{}\nYeni ssd giriniz:".format(self.pc[secim]["ssd"])))
                    self.pc[secim]["ssd"] = ssd
                    print("Ssd başarıyla değiştirildi...")
                    break
                else:
                    print("lütfen doğru sayıyı giriniz...")
            except ValueError:
                print("Sayı giriniz...")

    def __str__(self):
        return self.pc

    def __len__(self):
        return len(self.pc)


pc = Bilgisayar()
Durum = True
while Durum:
    secim = input("""
        Bilgisayarlar
        
1-Bilgisayarları Göster

2-Bilgisayar ekle

3-Bilgisayar çıkar

4-Bilgisayar fiyat değiştir

5- Bilgisayar ssd değiştir

6- Bilgisayar ram değiştir

7-Mevcut bilgisayar stoğu göster

0-Çıkış
             
secim:""")
    if secim == "0":
        break
    elif secim == "1":
        pc.bilgisayarları_göster()
    elif secim == "2":
        marka = input("Marka giriniz:")
        işlemci = input("İşlemci giriniz:")
        ekran_kartı = input("Ekran kartı giriniz:")
        while True:
            try:
                ram = int(input("Ram giriniz:"))
                ssd = int(input("Ssd giriniz:"))
                fiyat = float(input("Fiyat giriniz:"))
                break
            except ValueError:
                print("sayı giriniz...")
        pc.bilgisayar_ekle(marka, işlemci, ekran_kartı, ram, ssd, fiyat)
    elif secim == "3":
        pc.bilgisayar_çıkar()
    elif secim == "4":
        pc.fiyat_değiştir()
    elif secim == "5":
        pc.ssd_değiştir()
    elif secim == "6":
        pc.ram_değiştir()
    elif secim == "7":
        print(len(pc))
    else:
        print("Hatalı kodlama")
