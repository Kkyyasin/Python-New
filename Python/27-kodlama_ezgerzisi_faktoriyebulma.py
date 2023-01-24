durum = True
while durum:
    işlem = input("""
                Faktoriyel Bulma Programı
    
    1-Faktoriyel bul
    2-Çıkış

seçim:""")
    if işlem == "1":
        sayi = int(input("Faktoriyelini bulmak istediğiniz sayıyı giriniz:"))
        f = 1
        for i in range(1, sayi+1):
            f *= i
        print("{}!={}".format(sayi, f))
    elif işlem == "2":
        durum = False
    else:
        print("Hatalı Kodlama...")
print("\nProgram sonlandı...")
