from random import randint
sayi=randint(1,100)
for i in range(7):
    tahmin=int(input("{} tahmin hakkinizi giriniz:".format(i+1)))
    if tahmin>sayi:
        print("buyuk girdiniz tekrar deneyiniz")
    elif tahmin<sayi:
        print("kucuk girdiniz tekrar deneyiniz")
    else:
        print("Tebrikler sayiyi buldunuz sati:{}".format(tahmin))
        break

if i==6:
   print("bilemediniz")
