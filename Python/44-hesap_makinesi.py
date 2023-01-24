from math import *
while True:
    secim = input("""\n
     x   +   -   /   AC
     1   2   3   4   0

     %  x^2   x^(0.5)
     5   6    7

     sin  cos  tan  cot
      8    9   10   11

secim:""")
    if secim == "0":
        break
    elif secim == "1":
        m = int(input("girmek istediğiniz sayı miktarini giriniz:"))
        s = 1
        liste = list()
        for i in range(m):
            sayı = int(input("{}-sayıyı giriniz:".format(i+1)))
            s *= sayı
            liste.append(sayı)
        print(*liste, "sayıların çarpımı=", s)
    elif secim == "2":
        m = int(input("girmek istediğiniz sayı miktarini giriniz:"))
        t = 0
        liste = list()
        for i in range(m):
            sayı = int(input("{}-sayıyı giriniz:".format(i+1)))
            t += sayı
            liste.append(sayı)
        print(*liste, "sayıların Toplamı=", t)

    elif secim == "3":
        m = int(input("girmek istediğiniz sayı miktarini giriniz:"))
        liste = list()
        for i in range(m):
            sayı = int(input("{}-sayıyı giriniz:".format(i+1)))
            if i == 0:
                t = sayı
            else:
                t -= sayı
            liste.append(sayı)
        print(*liste, "sayıların Farkı=", t)
    elif secim == "4":
        m = int(input("girmek istediğiniz sayı miktarini giriniz:"))
        liste = list()
        for i in range(m):
            sayı = int(input("{}-sayıyı giriniz:".format(i+1)))
            if i == 0:
                s = sayı
            else:
                s /= sayı
            liste.append(sayı)
        print(*liste, "sayıların Bolumu=", s)
    elif secim == "5":
        liste = list()
        for i in range(2):
            sayı = int(input("{}-sayıyı giriniz:".format(i+1)))
            if i == 0:
                s = sayı
            else:
                s %= sayı
            liste.append(sayı)
        print(*liste, "sayıların Modu=", s)
    elif secim == "6":
        sayı = int(input("Karesini almak istediğiniz sayıyıy giriniz:"))
        print("{} karesi={}".format(sayı, sayı**2))
    elif secim == "7":
        sayı = int(input("Karekökünü almak istediğiniz sayıyı giriniz:"))
        print("{} karekökü={}".format(sayı, sayı**0.5))
    elif secim == "8":
        açı = float(input("Açı:"))
        print("sin {} ={}".format(açı, sin(açı)))
    elif secim == "9":
        açı = float(input("Açı:"))
        print("cos {} ={}".format(açı, cos(açı)))
    elif secim == "10":
        açı = float(input("Açı:"))
        print("tan {} ={}".format(açı, tan(açı)))
    elif secim == "11":
        açı = float(input("Açı:"))
        print("cot {} ={}".format(açı, 1/tan(açı)))
    else:
        print("Hatalı Kodlama...")
