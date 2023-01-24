"""Problem 2
Kullanıcıdan aldığınız boy ve kilo değerlerine göre kullanıcının beden kitle indeksini bulun.

Beden Kitle İndeksi : Kilo / Boy(m) Boy(m)
    """
kilo = float(input("Kilo giriniz:"))
boy = float(input("Boy giriniz:"))
Beden_kitle_endeksi = kilo/(boy**2)
print("Beden Kitle Endeksi:"+str(Beden_kitle_endeksi))
