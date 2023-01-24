import numpy as np
# Linear cebir modülüdür
# array matris işlemleri yapılır genelde
# ?Neden Numpy
#!Listeler göre az yer kaplar
#!Array elemanlarına daha hızlı
#!Ek metotları vardır
# ?array değikenleri referans olarak değişkenlerdir yani referansı başka değişkene eşitlendiğinde değiştiğinde diğeri de değişir
# Bunun için onlem larak copy metodu çözüm olur
# Array oluşturma
liste = [1, 2, 3, 4, 5, 6, 7, 8]  # Listeyi array yapmak
array = np.array(liste)
print(array)
array2 = np.array([1, 5, 8, 9, 10, 11, 12, 13, 14, 15, 16])  # array olusturma
array3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                  )  # 3x3 luk matris olusturur
print(array2)
print(array3)
