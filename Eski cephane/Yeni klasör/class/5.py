from random import *

class Personel():
    def __init__(self,ad,soyad,maas):
        self.ad=ad
        self.soyad=soyad
        self.maas=maas
        with open("personel.txt","r") as dosya:
            a=dosya.readlines()
        self.personeller=a
    def __str__(self):
        return """
    ad:{}
    soyad:{}
    maas:{}
        """.format(self.ad,self.soyad,self.maas)
class Yonetici(Personel):#personel  butun fonksiyonları kullanmayı sağlar
    def __init__(self,ad,soyad,maas):
        super().__init__(ad,soyad,maas)
    def personelekle(self):
        ad=input("add giriniz:")
        soyad=input("soyad giriniz:")
        maas=int(input("maas giriniz:"))
        if len(self.personeller) !=0:
         s = int(self.personeller[-1].split("-")[0])+1
        else:
            s=1
        self.personeller.append("{}-{} {} {}\n".format(s,ad,soyad,maas))
        print(s)
        for p in self.personeller:
         with open("personel.txt","w") as dosya:
            dosya.seek(0)
            dosya.writelines(p)

    def maasarttır(self,personel,artış=1000):
        personel.maas+=artış
personel=Personel("mehmet","özdemir",1005)
yonetici=Yonetici("yasin","özdemir",5000)
yonetici.maasarttır(personel)#maas artar
yonetici.personelekle()
print(personel)
print(yonetici)

