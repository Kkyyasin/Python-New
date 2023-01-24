liste1 = [*range(10)]
print(liste1)
liste2 = list()  # bos liste
for i in liste1:
    liste2.append(i)
print(liste2)
# list comprehension pratik bir şekilde liste oluşturur
liste3 = [1, 2, 3, 4, 5, 6]
liste4 = [i for i in liste3]
print(liste4)
liste5 = liste3
print(liste5)
liste6 = [i*2 for i in range(5)]
liste = [(1, 2), (3, 3), (3, 3)]
liste7 = [i*j for i, j in liste]
print(liste7)
print(liste6)
liste8 = list()
for i in liste:
    for j in i:
        liste8.append(j)
print(liste8)
# list comprehension ile
liste9 = [x for i in liste for x in i]
print(liste9)
