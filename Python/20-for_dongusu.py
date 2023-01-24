# in operatoru varlığı kontrol eder
print(5 in [1, 2, 3, 4])
print(5 in [1, 2, 3, 4, 5])
print("p" in "python")
liste = [1, 2, 3, 4, 5, 6]
toplam = 0
for eleman in liste:
    print("Eleman", eleman)
    toplam += eleman
print("toplam", toplam)
for i in range(1, 15, 2):
    print(i)
liste = range(1, 20)
for i in liste:
    if i % 2 == 0:
        print(i)
print(sum(range(1, 15)))
for i in "python":
    print(i*3, end="-")
liste = [(1, 2), (3, 4), (5, 6), (7, 8), (9, 10)]
for i, j in liste:
    print(i, j)
# dict gezinme
sozluk = {"isim": "Yasin", "Soyad": "Özdemir", "Yaş:": 18}
for i in sozluk:
    print(i)
for i in sozluk.values():
    print(i)
for i, j in sozluk.items():
    print(i+":"+str(j))
