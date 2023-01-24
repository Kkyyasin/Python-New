class Hayvan():
    def __init__(self, isim, cinsiyet, renk):
        self.isim = isim
        self.renk = renk
        self.cinsiyet = cinsiyet

    """def __init__(self):
        print("Paremetresiz")"""

    def __str__(self):
        return """
    Ad : {}
    Cinsiyet : {}
    Renk : {}""".format(self.isim, self.cinsiyet, self.renk)

    def isimDegistir(self, newname):
        self.isim = newname
        print("İsim değişti...")


class Kopek(Hayvan):

    def __init__(self, isim, cinsiyet, renk, dis_sayisi):
        super().__init__(isim, cinsiyet, renk)
        self.dis_sayisi = dis_sayisi

    def __str__(self):
        return super().__str__()+"\nDiş sayısı : {}".format(self.dis_sayisi)


class Kedi(Hayvan):
    def __init__(self, isim, cinsiyet, renk, göz_rengi):
        super().__init__(isim, cinsiyet, renk)
        self.goz = göz_rengi
        self.static()
        self.s += 1

    @staticmethod
    def static(self):
        self.s = 0

    def sta(self):
        print(self.s)


k = Kopek("Karabas", "Erkek", "Kahverengi", 4)
print(k)
k1 = Kedi("sjs", "dsd", "defı", "hefhu")
k2 = Kedi("sjs", "dsd", "defı", "hefhu")
k3 = Kedi("sjs", "dsd", "defı", "hefhu")
k3 = Kedi("sjs", "dsd", "defı", "hefhu")
k4 = Kedi("sjs", "dsd", "defı", "hefhu")
k4.sta()
