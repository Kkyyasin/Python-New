import time
import random
print("""
      *******************************
      
             Sayı Tahmin Oyunu
             
      *******************************
      """)
hak = 10
rasgele_sayı = random.randint(1, 40)
while hak != 0:
    tahmin = int(input("{}-hakkınızı giriniz:".format(11-hak)))
    if tahmin > rasgele_sayı:
        print("Kontrol ediliyor...")
        time.sleep(1)
        print("Daha düşük bir sayı giriniz...")
        hak -= 1
    elif tahmin < rasgele_sayı:
        print("Kontrol ediliyor...")
        time.sleep(1)
        print("Daha büyük bir sayı giriniz...")
        hak -= 1
    else:
        print("Kontrol ediliyor...")
        time.sleep(1)
        print("Tebrikler! sayıyı buldunuz...")
        break
if hak == 0:
    print("Maalesef bilemediniz")
