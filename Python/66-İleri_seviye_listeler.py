# append en sona eleman ekler
liste = [1, 2, 3, 4, 5, 6, 7, 8, 9]
liste.append(10)
print(liste)
# extend en sona liste ekler
liste1 = [1, 2, 3]
liste.extend(liste1)
print(liste)
# insert girilen indise eleman ekler
liste.insert(0, "Python")
print(liste)
# pop indis girilmesse sondan eleman siler
liste.pop()  # sondakini siler
liste.pop(2)  # 2 indisi siler
print(liste)
# remove girilen elamanı siler
liste.remove("Python")
# index metodu girilen eleman kaçıncı indiste olduğunu bulur
print(liste.index(4))
# count girilen değeri sayar
print(liste.count(2))
# sort sıralar
liste.sort()
print(liste)
