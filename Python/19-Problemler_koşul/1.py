"""Problem 1
Kullanıcıdan alınan boy ve kilo değerlerine göre beden kitle indeksini hesaplayın ve şu kurallara göre ekrana şu yazıları yazdırın.

 Beden Kitle İndeksi: Kilo / Boy(m) *  Boy(m)

 BKİ 18.5'un altındaysa -------> Zayıf

 BKİ 18.5 ile 25 arasındaysa ------> Normal

 BKİ 25 ile 30 arasındaysa --------> Fazla Kilolu

 BKİ 30'un üstündeyse -------------> Obez
"""
boy = float(input("Boy giriniz:"))
kilo = float(input("Kilo giriniz:"))
beden_kitle_endeksi = kilo/(boy**2)
if beden_kitle_endeksi < 18.5:
    print("Zayıf")
elif beden_kitle_endeksi < 25:
    print("Normal")
elif beden_kitle_endeksi < 30:
    print("Fazla Kilolu")
else:
    print("Fazla kilolu")
