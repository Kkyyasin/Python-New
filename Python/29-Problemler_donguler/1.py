"""
Problem 1
Kullanıcıdan aldığınız bir sayının mükemmel olup olmadığını bulmaya çalışın.

Bir sayının kendi hariç bölenlerinin toplamı kendine eşitse bu sayıya "mükemmel sayı" denir. Örnek olarak, 6 mükemmel bir sayıdır. (1 + 2 + 3 = 6)
"""
sayi = int(input("sayi giriniz:"))
toplam = 0
for i in range(1, sayi):
    if sayi % i == 0:
        toplam += i
        print(i)
if toplam == sayi:
    print("{} sayisi mükemmel sayı".format(sayi))
else:
    print("{} sayisi mükemmel sayı değildir".format(sayi))
