# liste tanımlamak
liste = ["merhab", 5, True]  # boyle tanımlanabiri içine bir çok değer alır
liste2 = list()  # bos liste tanımlamak
liste3 = []  # bos liste tanımlamak 2
liste4 = ["Ali", "Veli", ["Ayşe", "Nazan", "Zeynep"],
          34, 65, 33, 5.6]  # liste içinde liste olabilir
print(liste)
# yıldız bize eleman eleman ayırmamızı sağlar sep metodu ile arasını belirlenebilir
print(*liste)
sayılar = [[0, 10], [6, 60], [12, 54], [67, 99]]

for i in sayılar:
    print(*range(*i))  # girilen aralıkta bosluklu yazdırı alt satıra gecer
# range(s1,s2,s3) liste olusturur s1 bas değerinde s2 son değerine s3 de arttırma değeri yazılmassa default 1
print(*range(10))
# ? bu kullanım sınavda yarabilir 1 ve 10 arası listye atama
liste5 = [*range(1, 10)]
print(liste5)
kelime = "sms"
# her karekter eleman olarak stringden list kelimesiyle çevirdik
print(list(kelime))
# liste elemanlara erişim
meyveler = ["elma", "armut", "çilek", "kiraz"]
print(meyveler[0])  # ilk eleman
print(meyveler[:2])  # 2 indise kadar yazdırır
print(meyveler[2:])
print(meyveler[::-1])  # ters çevirir
# len anahtar kelimesi eleman ssayısı ogrenir listenin
print(len(meyveler))
meyveler[0] = "seftali"  # boyle elemanı değiştirebiliriz
# metodsuz eleman ekleme liste
meyveler += ["Kavun"]
print(*meyveler)
meyveler[0:2] = "muz", "kestane"  # ilk 2 elemanı değiştiryoz
print(meyveler)
# liste birleştirme
derlenen_diller = ["C", "C++", "C#", "Java"]
yorumlanan_diller = ["Python", "Perl", "Ruby"]
programlama_dilleri = derlenen_diller+yorumlanan_diller  # liste birleşir
print(programlama_dilleri)  # ilk hangisi gelirse o
# liste kopyalama
liste6 = liste5  # kopyalanır değeri değişşe bile diğeri değişmez
liste = [i for i in range(10) if i % 2 == 0 and i % 3 == 0]
print(liste)
matris = [[i, j] for i in range(10) for j in range(10)]
for i, j in enumerate(matris):
    print(*j, end="", sep="  ")
    if(i % 10 == 0):
        print()
