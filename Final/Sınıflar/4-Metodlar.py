class Kitap():
    def __init__(self, ad, sayfa_sayisi, yazar="Bilinmiyor"):
        self.sayfa_sayisi = sayfa_sayisi
        self.yazar = yazar
        self.ad = ad

    def __str__(self):
        return "Ad:{}\nSayfa sayısı:{}\nYazar:{}".format(self.ad, self.sayfa_sayisi, self.yazar)

    def __del__(self):
        print(self.ad+" adlı Kitap Silindi")

    def __len__(self):
        return len(self.sayfa_sayisi)

    def __eq__(self, other):
        if isinstance(other, Kitap):  # isinstance Classa aitmş kontrol eder
            return self.sayfa_sayisi == other.sayfa_sayisi
        return False


class MyClass:
    def __init__(self, value):
        self.value = value

    def __repr__(self):
        return f"{self.value}"  # basına f konularak yapılır


obj = MyClass(5)
print(obj)  # MyClass(5)
kitap1 = Kitap("assa", 5550)
kitap2 = Kitap("xxs", 4554, "asjs")
kitap3 = Kitap("xcdsw0", 5550, "ws")
print(kitap1.__str__())
print(kitap2.__str__())
print(kitap3.__str__())
if kitap1 != kitap2:
    print("esit değli")
if kitap3 == kitap1:
    print("eşit")
