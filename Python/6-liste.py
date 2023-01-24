liste = ["merhaba", 5, 8, 3.14]
bosliste = []
print(liste)
print(type(bosliste))
print(len(liste))  # uzunluk bulur
print(list("Merhaba"))
liste = [5, 5, 5, 2, 2, 4]
print(liste[2])
print(liste[-1])
print(liste[2:])
print(liste[::2])
print(liste[::-1])
liste1 = [1, 2, 3]
liste2 = [4, 5, 6]
print(liste1+liste2)
print(liste1*3)
liste2[1] = 7
print(liste2)
liste1[:2] = [55, 22]
print(liste1)
liste.append("python")  # ekleme
print(liste)
liste.pop()  # son elemanı silme
liste.pop(0)  # 0 indisi silme
print(liste)
liste.sort(reverse=True)  # sıralama
print(liste)
# iç içe listeler
liste3 = [[1, 2],  [1, 4]]
print(liste3)
print(liste3[0])
for i in liste3:
    for j in i:
        print(j, end="\t")
    print()
liste = [1, 1, 2, 2, 3, 3]
print(set(liste))  # tekrar etmeyecek sekilde olusturur
liste.remove(2)  # girilen elemanı cıkarır
print(liste)
print(liste.index(2))#girlen elemanın kacıncı indeste bulur
