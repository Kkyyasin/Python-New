liste = [i for i in dir(list) if not"_" in i]
print(liste)  # inceleyeceğimiz metodlar
# append eleman eklemeye yarar sona ekler
liste2 = list()
liste2.append("sk")  # string eklendş
print(liste2)
liste2.append(5)
print(liste2)
liste2 += [74]
# extend liste gibi çok kapsamlı seyler ekler sona
liste3 = [*range(5)]
liste2.extend(liste3)  # liste eklendi
print(liste2)
# insert indis belirlereyer eklemey yarar
liste2.insert(1, "Yasin")
print(liste2)
# remove silmeye yara
liste2.remove(4)  # 4 sayısı siler
liste2.remove("Yasin")
liste2.remove("sk")
# pop indisi siler
liste2.pop(3)
liste2.sort()  # sıralar ama hepsi aynı tur olursa

print(liste2)
# index indexi ogrenir
liste2.insert(2, "Merhaba")
print(liste2.index("Merhaba"))  # olmayan girilirse hata verir
# count kac kez gectiğini sayar
print(liste2.count(2))
# clear listeyi bosaltır
liste2.clear()
print(liste2)
