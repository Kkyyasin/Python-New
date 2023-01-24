#string ifadeler
yazi="merhaba dunya"
print(yazi)
yazi1="""
merhhajs kakso 
cmodsk
cops
"""#coklu uzun metin yazdirmak için""" """ tirnak arasi kullanilir
print(yazi1)
print(yazi.replace("a","e"))#harfleridegistermek icin kullanılır
print(yazi[0])#dizinin 0 indiskindeki harfi alır
print(yazi[2:8])#2 ile 8 indissi arasini alır
print(yazi[2:8:3])#2 baslangıc 8 son 3 atlama(artış degeri)
isim="yasin"
uzunluk=len(isim)
print(uzunluk)
metin="yasin odevleri yapti"
print(metin[uzunluk:len(metin):2])#uzunluk baslangiç len(metin)son 2atlma
print(metin[::-1])#-1 ler geri geri okutma
print(len(metin))#karektersayisi ogrenme
print(metin[-1])
ad="yasin"
soyad="ozdemir"
print(5*(ad+" "+soyad))#karekter birlestirilebilir toplam ile *ile tekralandirabilir
toplam=ad+soyad
print(toplam)
print(ad.upper())

print("Merhaba".lower())
print("merhaba dunya".split())
print("merr aja".split("r"))#girilen degerde liste gibi ayirir
