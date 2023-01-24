class Araba():
    model = "Ford Focus"
    renk = "Beyaz"
    beygir_gücü = 130
    silindir = 4
    fiyat = 350000


araba = Araba()  # araba objesi oluşturduk
print(araba)
print(type(araba))
print(araba.model)  # erişim nokta ile sağlanıyor
print(araba.renk)
print(araba.beygir_gücü)
print(araba.silindir)
print(araba.fiyat)
print(Araba.model)
# __init__() fonksiyonu obje oluşturulduğunda yapılan işlemler


class Tır():
    def __init__(self, model="Bilgi yok", fiyat="Bilgi yok", renk="Bilgi yok"):  # self referansdır
        print("Bu fonksiyon çalıştı")
        self.model = model
        self.fiyat = fiyat
        self.renk = renk


tır1 = Tır("Volvo", 250000, "Siyah")
tır2 = Tır("Scania", 220000, "Beyaz")
tır3 = Tır("Man", 200000, "Beyaz")
tır4 = Tır()
tır5 = Tır(renk="yeşil")
print(tır1.model, tır1.fiyat, tır1.renk)
print(tır2.model, tır2.fiyat, tır2.renk)
print(tır3.model, tır3.fiyat, tır3.renk)
print(tır4.model, tır4.fiyat, tır4.renk)
print(tır5.model, tır5.fiyat, tır5.renk)
