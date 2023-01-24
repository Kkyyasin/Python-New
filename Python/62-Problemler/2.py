"""Elinizden her bir elemanı 3'lü bir demet olan bir liste olsun.

     [(3,4,5),(6,8,10),(3,10,7)]

Şimdi kenar uzunluklarına göre bu kenarların bir üçgen olup olmadığını dönen bir fonksiyon yazın ve sadece üçgen belirten kenarları bulunduran listeyi ekrana yazdırın.

     [(3, 4, 5), (6, 8, 10)]

Not: filter() fonksiyonunu kullanmaya çalışın."""


def ucgenmi(i):
    x, y, z = i[0], i[1], i[2]
    print(x-y)
    if abs(x-y) < z < x+y and abs(y-z) < x < y+z and abs(z-x) < y < x+z:
        return True
    else:
        return False


liste = [(3, 4, 5), (6, 5, 10), (3, 10, 7)]

print(list(filter(ucgenmi, liste)))
