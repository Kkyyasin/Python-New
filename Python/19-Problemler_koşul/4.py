"""
Problem 4
Şimdi de geometrik şekil hesaplama işlemi yapalım. İlk olarak kullanıcıdan üçgenin mi dörtgenin mi tipini bulmak istediğini sorun.

Eğer kullanıcı "Dörtgen" cevabını verirse , 4 tane kenar isteyip bu dörtgenin kare mi , dikdörtgen mi yoksa sıradan bir dörtgen mi olduğunu bulmaya çalışın.

Eğer kullanıcı "Üçgen" cevabını verirse , 3 tane kenar isteyip bu üçgenin ikizkenar mı , eşkenar mı yoksa sıradan bir üçgen mi olduğunu bulmaya çalışın. Eğer verilen kenarlar bir üçgen belirtmiyorsa, ekrana "Üçgen belirtmiyor" şeklinde bir yazı yazın.o

Üçgen belirtme şartını bilmiyorsunuz internetten bakabilirsiniz.

Ayrıca , bu problemde mutlak değer bulmaya ihtiyacınız olacak. Bunun için, Pythonda hazır bir fonksiyon olan abs() fonksiyonunu kullanabilirsiniz. Kullanımı şu şekildedir ;
"""
while True:
    sekil = input(""""
            1-Üçgen
            2-Dörtgen
            3-Çıkış
            
    seçim:""")
    if sekil == "1":
        k1 = int(input("1-Kenar giriniz:"))
        k2 = int(input("2-Kenar giriniz:"))
        k3 = int(input("3-Kenar giriniz:"))
        if k1 < k2+k3 and k1 > abs(k2-k3) and k2 < k1+k3 and k2 > abs(k1-k3) and k3 < k1+k2 and k3 > abs(k2-k1):
            if k1 == k2 == k3:
                print("eşkenar üçgen")
            elif k1 == k2 or k2 == k3 or k1 == k3:
                print("İkizkenar üçgen")
            else:
                print("Çeşitkenar üçgen")
        else:
            print("Üçgen belirtmiyor")
    elif sekil == "2":
        k1 = int(input("1-Kenar giriniz:"))
        k2 = int(input("2-Kenar giriniz:"))
        k3 = int(input("3-Kenar giriniz:"))
        k4 = int(input("4-Kenar giriniz:"))
        if k1 == k2 == k3 == k4:
            print("kare")
        elif k1 == k3 and k2 == k4:
            print("Dikdörtgen")
        else:
            print("Yamuk")
    elif sekil == "3":
        break
    else:
        print("Hatali kodlama")
