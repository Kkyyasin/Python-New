def kayıt_oluştur(isim, soyisim, işsis, şehir):
    print("-"*30)

    print("isim           : ", isim)
    print("soyisim        : ", soyisim)
    print("işletim sistemi: ", işsis)
    print("şehir          : ", şehir)

    print("-"*30)


kayıt_oluştur("Fırat", "Özgül", "Ubuntu", "İstanbul")
kayıt_oluştur("Mehmet", "Öztaban", "Debian", "Ankara")
kayıt_oluştur("İlkay", "Kaya", "Mint", "Adana")
kayıt_oluştur("Seda", "Kara", "SuSe", "Erzurum")  # def le olusur


def fonksiyon(*parametreler):  # istediğn kadar girebiliyon
    print(parametreler)


print(fonksiyon(1, 2, 3, 4, 5))  # None değer dondurur
#global deyimi
x = 0


def fonk():
    x = 1  # x fonksyon içinde olduğu içind eğişmez
    print(x)


y = 4
z = 2


def fonk2():
    global y
    y = 5
    print(y)


def fonk3():
    print(z)


fonk()
print(x)
fonk2()
print(y)
fonk3()
