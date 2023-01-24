import time


def kare_hesapla(sayılar):
    sonuc = list()
    bas = time.time()
    for i in sayılar:
        sonuc.append(i**2)
    son = time.time()
    print("kare"+" "+"fonksiyonu" + str(son-bas)+" sn ye surdu")
    return sonuc


def kup_hesapla(sayılar):
    sonuc = list()
    bas = time.time()
    for i in sayılar:
        sonuc.append(i**3)
    son = time.time()
    print("kup"+" "+"fonksiyonu" + str(son-bas)+" sn ye surdu")
    return sonuc


def zaman_hesapla(func):  # fonsiyon gonderilir
    def wrapper(sayılar):  # decoreter fonsiyon için mutlaka wrapper tanımlanmalı
        bas = time.time()
        sonuc = func(sayılar)  # sonuc alınır
        son = time.time()
        print(func.__name__+" "+"fonksiyonu" + str(son-bas)+" sn ye surdu")
        return sonuc  # sonuc doner
    return wrapper  # bu olmalı
# decoreter fonsiyon ortak kullanılan metodların fonksiyonlara gonderilmesi


kare_hesapla(range(1000000))
kup_hesapla(range(1000000))


@zaman_hesapla
def karee_hesapla(sayılar):
    sonuc = list()

    for i in sayılar:
        sonuc.append(i**2)
    son = time.time()

    return sonuc


@zaman_hesapla
def kupp_hesapla(sayılar):
    sonuc = list()
    for i in sayılar:
        sonuc.append(i**3)

    return sonuc


kupp_hesapla(range(1000000))
karee_hesapla(range(1000000))
