
class Dosya():
    def __init__(self):
        print("nns")
        with open("metin.txt", "r", encoding="utf-8") as file:
            li = file.read()
            liste = li.split()
            self.kelimeler = list()
            for i in liste:
                i = i.strip(" ")
                i = i.strip(".")
                i = i.strip(",")
                self.kelimeler.append(i)

    def Tum_kelimeler(self):
        kelime_kumesi = set()
        for i in self.kelimeler:
            kelime_kumesi.add(i)
        for i in kelime_kumesi:
            print(i)

    def kelime_frekansı(self):
        frekans = dict()
        for i in self.kelimeler:  # varlığını kontrol ederiyoruz
            if i in frekans:
                frekans[i] += 1
            else:
                frekans[i] = 1
        for i, j in frekans.items():
            print("{} kelimesi {} defa geciyor".format(i, j))


dosya = Dosya()
dosya.Tum_kelimeler()
dosya.kelime_frekansı()
