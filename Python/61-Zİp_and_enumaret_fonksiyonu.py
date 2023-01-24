liste1 = [1, 2, 3, 4, 5]
liste2 = [6, 7, 8, 9, 10, 11, 12]
print(list(zip(liste1, liste2)))  # zip birleştiririr
# [(1,6),(2,7),(3,8),(4,9),(5,10)]
liste3 = ["me", "kkk", "ld", "ss"]
print(list(zip(liste1, liste2, liste3)))
for i, j, k in zip(liste1, liste2, liste3):
    print(i, j, k)
# enumurate  numaralandırır
print(list(enumerate(liste3)))
for i, j in enumerate(liste3):
    print(i+1, j)
# all herhangi bir değer false false heps true ise true dondururur
# any tam tersi
print(all([True, False, False]))
print(all([True, True]))
print(any([False, False]))
print(any([False, True]))
