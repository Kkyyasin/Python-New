print("**********\nKullanıcı Girişi\n**********\n")
sys_kullanıcı_adı = "kkyyasin"
sys_parola = "12345"
giris_hakkı = 5
while True:
    kullanıcı_adı = input("Kullanıcı Adı:")
    passopord = input("Parola:")
    if kullanıcı_adı == sys_kullanıcı_adı:
        if sys_parola == passopord:
            print("Hoşgeldiniz")
            break
    elif giris_hakkı == 0:
        print("Maalesef giriş hakkınız bitti daha sonra tekrar deneyiniz")
        break

    print("Tekrar deneyiniz lutfen {} hakkınız kaldı".format(giris_hakkı))
    giris_hakkı -= 1
