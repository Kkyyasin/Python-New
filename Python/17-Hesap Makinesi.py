while True:
    islem = int(input("""
********************************************
            Hesap Makinesi
    
    0. Çıkış
    
    1. Toplama İşlemleri
    
    2. Çıkarma İşlemleri

    3. Çarpma İşlemleri
    
    4. Bölme İŞlemleri

Yapmak istediğiniz işlemi seçiniz:"""))
    a = int(input("Birinci Sayıyı giriniz:"))
    b = int(input("İkinci Sayıyı giriniz:"))
    print("Sonuç:", end="")
    if islem == 0:
        break
    elif islem == 1:
        print(a+b)
    elif islem == 2:
        print(a-b)
    elif islem == 3:
        print(a*b)
    elif islem == 4:
        print(a/b)
    else:
        print("Hatalı şeçim tekrar deneyiniz.")
