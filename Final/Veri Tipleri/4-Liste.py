import random
liste = [i for i in dir(list) if not"_" in i]
print(liste)  # inceleyeceğimiz metodlar

# append() ekleme yapar
liste = []
liste.append("skds0")
liste.append(5)
liste += [5]  # ek olarak metot suz ekleme yapar
print(liste)

# extend liste ye liste ekler
liste2 = [*range(5)]
liste.extend(liste2)
print(liste)  # sona ekler

# insert() indise gore ekleme yapar
liste.insert(1, "Yasin")
print(liste)

# remove silmeye yarar
liste.remove(2)  # 2 sayısı siler
liste.remove("Yasin")

# pop indisi siler
liste2.pop(3)
liste3 = [random.randrange(0, 100) for i in range(20)]
print(liste3)
liste3.sort()  # sıralar ama hepsi aynı tur olursa
print(liste3)

# count kac kez gectiğini sayar
print(liste.count(4))

# clear listeyi bosaltır
liste.clear()
print(liste)
print(liste.__contains__(2))  # varlgı kontrol eder
