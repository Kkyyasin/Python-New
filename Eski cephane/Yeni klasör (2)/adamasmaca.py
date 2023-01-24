from random import choice,randint
import string
string.
kelimeler=["araba","kamyon","makine"]
oyun=True

    kelime = choice(kelimeler)
    tahmin = kelime
    hak=2*len(tahmin)
    while True:
         tahmin = list()
         for i in range(0,3):
             tahmin[randint(0,hak/2-1)]="_"
         for i in range(hak):
          a=input("{} hakkinizi giriniz:".format(i+1))
          if a.__contains__(kelime):
              print("Tebrikler kelimeyi bildiniz kelime:{}".format(kelime))
              break
         if hak== i:
            print("kelimeyi bilemediniz")
            break
    secim=input("yeni oyun için e çıkmak için herhangi bir tusa basiniz")
    if secim=="e":
        oyun=True
    else:
        oyun=false
