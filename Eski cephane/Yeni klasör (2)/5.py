#sayinin bolenlerini bulma
sayi=int(input("sayi giriniz:"))
for i in range(1,sayi):
    if sayi%i==0:
        print(i)