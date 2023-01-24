import numpy as np

# numpy range metodu listelerdeki gibi belli aralıka array olusturur ama adı arange dir
array = np.arange(10, 20)  # 10 ie 20 arası değer olusturur
#!20 dahil değil
print(array)
array2 = np.arange(0, 100, 3)  # 0 100 arası 3 er 3 er
print(array2)

# ones metotu 1 ler olusurturur
print(np.ones(10))  # 10 tane 1 lerden olusana array olusturur
print(np.ones((4, 4)))  # 4x4 1 lerden olusan matris olusturur

# zeros 0 lar olusturur aynı mantık
print(np.zeros((4, 4)))
print(np.zeros((3, 2)))
# linspace
# 0 ile 100 arasını 5 e boler boldug değerleri yazdırır çıktı 0 ,25 ,50 ,75 ,100
print(np.linspace(0, 100, 5))
# eyes birim matris olusturur
print(np.eye(4, 4))

# ? Random değerler olusturma
# randint
print(np.random.randint(0, 10))  # 0 ile 10 arası random int değer dondurur
print(np.random.randint(15))  # 15 kadar rasgele değer olusturur
# 1 ile 10 arası ranodm değer olusturur 5 tane arraye atar
print(np.random.randint(1, 10, 5))
# rand
# virgullu degerler olusturur
print(np.random.rand(5))  # 5 e kadar olusturur

# randn - li değer olutuur ek olarak
print(np.random.randn(0, 5, 5))  # -5 ile 5 arası 5 değer atar
# choice
# rasgele listeden atar matrise
print(np.random.choice(["Mehmet", "Musta"], (2, 3)))
