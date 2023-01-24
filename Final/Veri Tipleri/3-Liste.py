# her turlu veri tipiyle karısık tanımlanabilir
liste = ["Muhammed", 1, True, 4.5]
liste1 = list()
liste1 = []  # bu sekilde tanımlanabilir
liste2 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"],
          34, 65, 33, 5.6]  # liste içinde liste olabilir
print(liste)
print(*liste)  # daha guzel gozukturur * dız sepl ede arası ayarlanabilir
print([*range(5)])  # 5 range aralğında liste olusur

metin = "Muhammed Yasin"
print(list(metin))  # her harf harf liste elemanına atar
meyveler = ["elma", "armut", "çilek", "kiraz"]

print(meyveler[0])  # ilk eleman
print(meyveler[:2])  # 1 indise kadar yazdırır#!2 dahil değil
print(meyveler[2:])
print(meyveler[::-1])  # ters çevirir
# len anahtar kelimesi eleman ssayısı ogrenir
meyveler[0] = "seftali"  # boyle elemanı değiştirebiliriz
derlenen_diller = ["C", "C++", "C#", "Java"]
yorumlanan_diller = ["Python", "Perl", "Ruby"]
programlama_dilleri = derlenen_diller+yorumlanan_diller  # liste birleşir
liste3 = [i for i in range(100) if i % 2 == 0 and i %
          3 == 0]  # list comprosion
print(liste3)
matris = [[i, j] for i in range(10) for j in range(10)]
for i in matris:
    for j in i:
        print(j, end="  ")
    print()
