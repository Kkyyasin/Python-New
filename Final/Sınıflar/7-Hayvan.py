# inherit
class Hayvan():
    def __init__(self, isim, kilo, boy, bacak_sayisi):
        self.isim = isim
        self.kilo = kilo
        self.boy = boy
        self.bacak_sayisi = bacak_sayisi

    def __str__(self):
        return """
    Isım:{}
    Kilo:{}
    Boy:{}
    Bacak:{}""".format(self.isim, self.kilo, self.boy, self.bacak_sayisi)

    def Yemek(self):
        print("Hayvan yemek yiyor...")

    def Konus(self):
        print("Hayvan konusuyor")


class Kopek(Hayvan):
    def __init__(self, isim, kilo, boy, bacak_sayisi):
        super().__init__(isim, kilo, boy, bacak_sayisi)
        self.tur = "Kopek"

    def Konus(self):
        print("Kopek konusuyor...")


class At(Hayvan):

    def Konus(self):
        print("At konusuyor...")

    def __str__(self):
        return """At
    Isım:{}
    Kilo:{}
    Boy:{}
    Bacak:{}""".format(self.isim, self.kilo, self.boy, self.bacak_sayisi)


class Kedi(Hayvan):
    def __init__(self, isim, kilo, boy, bacak_sayisi):
        super().__init__(isim, kilo, boy, bacak_sayisi)
        self.tur = "Kedi"

    def Konus(self):
        print("Kedi konusuyor...")


kedi = Kedi("Tekir", 45, 80, 4)
kopek = Kopek("pusat", 55, 80, 4)
at = At("Karayel", 75, 60, 4)
hayvan = Hayvan("Pamuk", 35, 20, 2)

print(kedi)
kedi.Konus()
kedi.Yemek()

print(kopek)
kopek.Konus()
kopek.Yemek()

print(at)
at.Konus()
at.Yemek()

print(hayvan)
hayvan.Konus()
hayvan.Yemek()
