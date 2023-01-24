#set yapısı
set1={"merhaba","naber","naber"}#set elemanlar tekrar etmez
print(type(set1))
print(set1)
print(len(set1))
set2 = set((1,1,2,3))
print(set2)
set3=set("merhabaa")
print(set3)#harfleri tekrar etmeyecek sekilde set yapısı olusturur
print(set2)
set2.add(4)#eleman ekler
print(set2)
set2.discard(3)#eleman siler
print(set2)
kume1={1,2,3,4,5}
kume2={4,5,6,7,8}
print(kume2.difference(kume1))#kume2 de olup kume1 de olmayanlar değişiklik olmaz
kume1.difference_update(kume2)#değişiklik olur
print(kume1)
kume3={1,2,3,4,5}
kume4={4,5,6,7,8}
print(kume3.intersection(kume4))#ortak noktalari verir
print(kume3.union(kume4))#birleşimini alır
