#kisi bilgisi olusturucu
kisibilgisi={}
while True:
    secim=int(input("1-kişi ekle\n2-kisi çıkar \n3-yazdır\nyapmak isteginiz scenegi seciniz:"))
    if secim==1:
        ad=input("ad giriniz:")
        soyad=list(input("soyad giriniz:"))
        kisibilgisi[ad]=soyad
    elif secim==2:
        kisi=input("cıkarmak istediginiz kisisyi girniz:")
        a=kisibilgisi.keys()
        b=list(a)
        b.remove(kisi)
        a=str(b)
        kisibilgisi
    else:break
    print(kisibilgisi)


