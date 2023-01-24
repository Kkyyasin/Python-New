class Araba():  # sıınf ollusturma
    model = "Ford Focus"  # keddimiz ilk basta burda deger veririz mainde değişir
    renk = "Beyaz"
    beygir = 130
    fiyat = 4200000


araba = Araba()  # nesne olusturlır
print(araba.model)
print(araba.renk)
print(araba.beygir)
print(araba.fiyat)
araba.fiyat = 5000000
print(araba.fiyat)


class Araba2():
    def __init__(self, marka, model, renk, fiyat):
        print("init metodu")
        self.marka = marka
        self.model = model
        self.renk = renk
        self.fiyat = fiyat


araba2 = Araba2("Ford", "Focus", "Beyaz", 455555)
print(araba2.model)
print(araba2.marka)
print(araba2.renk)
print(araba2.fiyat)
