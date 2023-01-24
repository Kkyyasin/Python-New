# kumeler aynı elamanı tek elemana indirger set ile gosterili
liste = [1, 1, 2, 3, 3, 4, 5]
x = set(liste)
print(x)
x = set("python programlama")
print(x)
x = {"p", "p", "a"}
print(x)
# kumeler for dongusunde gezinebilir ve kumeler sırasızdır indexlerle ulaşılmaz
x = set(liste)
for i in x:
    print(i)
# kume metodları add ekleme yapılıyor aynı eleman eklenirse herhangi süişlem yapılmıyor
x = {1, 2, 3, 4, 5}
x.add(6)
print(x)
x.add(4)
print(x)
# difference iki kumenin birbirinden farkı alır
kume1 = {1, 2, 3, 4, 5}
kume2 = {3, 4, 5, 6, 7}
print(kume1.difference(kume2))  # kume 1 kume 2 den farkı
print(kume2.difference(kume1))  # kume 2 kume 1 den farkı
# kume 1 kume 2 den farkını kume 1 e atar kumeyi günceller
kume1.difference_update(kume2)
print(kume1)
# discard kumeden elman cıkarır eleman yoksa hiç birşey yapmaz
print(kume2)
kume2.discard(6)
print(kume2)
kume2.discard(6)
print(kume2)
# intersection orta elemanları bulur
kume1.add(4)
print(kume1.intersection(kume2))
# kume 1 ortak olanları ile değiştirir gunceller
kume1.intersection_update(kume2)
# isdisjoint kumenin ayrıkmı değilmi kontrol eder keşişm bos sa ayrık true doner değilse false
print(kume1.isdisjoint(kume2))
# issubset kume kessim var ise true yok sa false alt kume yani
print(kume1.issubset(kume2))
# union iki kumenin birleşimi olarak doner
print(kume1.union(kume2))
# update metodu birleştirir aynı şekilde ilk  basta yazılana atar
kume1.update(kume2)
print(kume1)
