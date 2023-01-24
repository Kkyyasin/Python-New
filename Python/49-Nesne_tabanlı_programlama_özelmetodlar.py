class Kitap():
    def __init__(self, name, sayfa_sayısı, yazar):
        self.name = name
        self.sayfa_sayısı = sayfa_sayısı
        self.yazar = yazar

    def __str__(self):
        return "Ad:{}\nSayfa sayısı:{}\nYazar:{}".format(self.name, self.sayfa_sayısı, self.yazar)

    def __len__(self):
        return self.sayfa_sayısı

    def __del__(self):
        print("Kitap siliniyor....")


kitap = Kitap("İstanbul Hatırası", 561, "Ahmet Ümit")  # __init__ metodu
print(kitap)  # __str__ metodu
print(len(kitap))  # __len__ metodu
del kitap  # __del__ metodu del objeyi silmeye yarar
