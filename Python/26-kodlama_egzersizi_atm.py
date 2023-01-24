from re import M


bakiye = 5000
while True:
    işlem = input("""****************************************************
               ATM'ye Hoşgeldiniz
               
    İşlemler;
    
    1-Bakiye sorgulama
    
    2-Para Yatırma
    
    3-Para Çekme
    
    4-Çıkış
    
secim:""")
    if işlem == "1":
        print("Total Para:{} TL".format(bakiye))
    elif işlem == "2":
        miktar = float(input("Yatırmak istediğiniz miktarı giriniz:"))
        bakiye += miktar
        print("Para Başarıyla Yatırıldı.\nTotal Para:{} TL".format(bakiye))
    elif işlem == "3":
        miktar = float(input("Çekmek istediğiniz miktarı giriniz:"))
        if bakiye-miktar >= 0:
            bakiye -= miktar
            print(
                "Para çekme işlemi başarıyla tamamlandi.\nTotal Para:{} TL".format(bakiye))
        else:
            print("Yeterli baakiyeniz bulunmuyor")
    elif işlem == "4":
        print("Program sonlandı...")
        break
    else:
        print("Hatalı kodlama tekrar deneyiniz")
    print()
