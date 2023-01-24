#class yapısı ornek str,chr,list bizde oluşurabiliriz
class araba():
    def __init__(self,girilenmarka,girilenmodel,girilenfiyat,girilenyıl,girilenrenk):#sınıf cagrıldığında olusur
        self.marka=girilenmarka
        self.model=girilenmodel
        self.fiyat=girilenfiyat
        self.yıl=girilenyıl
        self.renk=girilenrenk
        print("{} araba markasi oluşturuldu".format(self.marka))
    def bilgilerigoster(self):
       return """
         1-Marka: {marka}
         2-Model: {model}
         3-Fiyat: {fiyat}
         4-Yıl: {yıl}
         5-Renk: {renk}
        """.format(marka=self.marka,model=self.model,fiyat=self.fiyat,yıl=self.yıl,renk=self.renk)
    def __str__(self):
        return  self.bilgilerigoster()
    def renkdegistir(self,girilenrenk):
        self.renk=girilenrenk
    def fiyatdegistir(self,girilenfiyat):
        self.fiyat = girilenfiyat
arabaa=list()
durum=True
dosya=open("araba.txt","w")
while durum:
    secim=int(input("""
    1-Araba ekleyin
    2-Araba cıkar
    3-Araba fiyat degistir
    4-Araba renk degistir
    5-Araba bilgileri göster
    6-herhangi bir tusa basarak cıkınız ve yazdirin
       secim:
    """))
    if secim==1:
        marka=input("marka giriniz:")
        model=input("model giriniz:")
        fiyat=input("fiyat giriniz:")
        yıl=input("yıl giriniz:")
        renk=input("renk giriniz:")
        arabaa.append(araba(marka,model,fiyat,yıl,renk))
        print(len(arabaa))
    elif secim==2:
        for i in range(len(arabaa)):
            print("{}-{} markasi {} modeli".format(i+1,arabaa[i].marka,arabaa[i].model))
        cıkar=int(input("cıkarmak istediğiniz markanin numarasini giriniz:"))
        if cıkar < len(arabaa)+1 and cıkar> -1:
             arabaa.pop(cıkar-1)
        else:
            print("hatali kodlama yaptiniz")
    elif secim==3:
        for i in range(len(arabaa)):
            print("{}-{} markasi {} modeli".format(i + 1, arabaa[i].marka, arabaa[i].model))
        fiyat=int(input("fiyati değistirmek istediğiniz araba numarısını giriniz:"))
        girilenfiyat=float(input("fiyat giriniz:"))
        if fiyat < 1+len(arabaa) and fiyat > -1:
             arabaa[fiyat-1].fiyatdegistir(girilenfiyat)
        else:
            print("hatali kodlama yaptiniz.")
    elif secim==4:
        for i in range(len(arabaa)):
            print("{}-{} markasi {} modeli".format(i + 1, arabaa[i].marka, arabaa[i].model))
        renk = int(input("rengi değistirmek istediğiniz araba numarısını giriniz:"))
        girilenrenk = input("renk giriniz:")
        if renk < len(arabaa)+1 and renk > -1:
           arabaa[renk-1].renkdegistir(girilenrenk)
        else:
            print("hatali kodlma yaptiniz.")
    elif secim==5:
        for i in range(len(arabaa)):
            print("{}-{} markasi {} modeli".format(i + 1, arabaa[i].marka, arabaa[i].model))
            bilgi=int(input("bilgilerini istedğiniz araba marka numarasini giriniz:\ncıkmak icin -1 tusuna basınız"))
            if len(arabaa)+1>bilgi or bilgi>-1:
               print(arabaa[bilgi-1].bilgilerigoster())
            elif bilgi==-1:
                break
            else:
                print("hatali kodlama yaptınız")
    elif secim==6:
        durum=False
    else:
        print("hatali kodlama")
print("------------ Arabalar ------------",file=dosya)
for i in range(len(arabaa)):
    print("{}-{} markasi {} modeli".format(i + 1, arabaa[i].marka, arabaa[i].model),file=dosya)
    print("{}".format(arabaa[i].bilgilerigoster()),file=dosya)






