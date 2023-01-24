while(True):
    secim = input("""
                1-Topla
                2-çıkart
                3-Çarp
                4-Bol
                5-Mod al
                6-Kare al
                7-Karekok al
    secim:""")
    if secim == "q":
        break
    if secim == "1":
        a, b = int(input("Birinic sayı giriniz:")), int(
            input("İkinci sayı giriniz:"))
        print(a+b)
    elif secim == "2":
        a, b = int(input("Birinic sayı giriniz:")), int(
            input("İkinci sayı giriniz:"))
        print(a-b)
    elif secim == "3":
        a, b = int(input("Birinic sayı giriniz:")), int(
            input("İkinci sayı giriniz:"))
        print(a*b)
    elif secim == "4":
        a, b = int(input("Birinic sayı giriniz:")), int(
            input("İkinci sayı giriniz:"))
        print(a/b)
    elif secim == "5":
        a, b = int(input("Birinic sayı giriniz:")), int(
            input("İkinci sayı giriniz:"))
        print(a % b)
    elif secim == "6":
        a = int(input(" sayı giriniz:"))
        print(a**2)
    elif secim == "7":
        a = int(input(" sayı giriniz:"))
        print(a**0.5)
    else:
        print("Hatalı kodlam...")
