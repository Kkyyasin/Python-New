class Personel():
    def __add__(self, other):
        return 10+other
    def __init__(self,ad,soyad,yas):
        self.ad=ad
        self.soyad=soyad
        self.yas=yas
    def __str__(self):
        return """
    ad:{}
    soyad:{}
    yas{}
        """.format(self.ad,self.soyad,self.yas)
    def __len__(self):
        for i in range(100):
            print(i)
        return 10
    def __int__(self):
        return 10

personel=Personel("muhammed yasin","özdemir",18)
print(personel)#str fonksiyonu sayesinde
print(personel+10)#add sayesinde
len(personel)
print(int(personel))#int halini cevirir

