a = [1, 2, 3, 4, 5]
a.append(-5)  # liste ye ekleme yapar
a.extend([1, 2, 3, 4, 5])  # liste ekler
print(a)
a.remove(-5)  # içine yazılanı siler
print(a)
a.pop(0)  # index yazılmassa sondan yazılırsa şeçili indexi siler
print(a)
a.sort()  # liste sıralar
print(a)
a.insert(2, "Merhaba")  # index ,eklenecek değer
print(a)
b = a.copy()  # listeyi kopyalar
print(b)
print(a.count("Merhaba"))  # varlığını kontrol eder
