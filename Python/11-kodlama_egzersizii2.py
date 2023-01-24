# ikinci dereceden denklem kok bulma
#denklem : ax^2+bx+c
# delta:b**2-4*a*c
# birinci kok :(-b-delta**5)/(2*a)
# ikinci kok :(-b+delta**5)/(2*a)
while True:
    try:
        a = float(input("x^2 Katsayısı"))
        b = float(input("x Katsayısı"))
        c = float(input("Sabit sayı Katsayısı"))
        break
    except ValueError:
        print("lutfen sayi giriniz")
delta = b**2-4*a*c
if delta > 0:
    kok1 = (-b-delta**0.5)/(2*a)
    kok2 = (-b+delta**0.5)/(2*a)
    print("kok1:{}\nkok2:{}".format(kok1, kok2))
elif delta == 0:
    kok = (-b-delta**0.5)/(2*a)
    print("Çift Kartlı Kök Vardır Kök:{}".format(kok))
else:
    print("Real Kök yoktur.")
