total = 2000
a = "myasin12345"
while True:
    sifre = input("kart sifresi giriniz:")
    if sifre == a:
        while True:
            secim = int(input("""
    1-para cekme
    2-para yatirma
    3-kart bilgileri
    4-kart iade
     secim:"""))
            if secim == 1:
                para = int(input("cekmek istediğiniz miktari giriniz:"))
                if para > total:
                    print("cekmek istediğiniz miktar fazla tekrar deneyiniz.")
                else:
                    total -= para
            elif secim == 2:
                para = int(input("yatirmak istediğiniz miktari giriniz:"))
                total += para
            elif secim == 3:
                print(
                    " kart sahibi:muhammed yasin özdemir\n toplam para:{}".format(total))
            else:
                print("kart iade ediliyor")
                break
    else:
        print("sifre yanliş tekrar deneyiniz")
