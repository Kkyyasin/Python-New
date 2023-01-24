import numpy as np
array = np.random.randint(1, 100, 10)  # 10 elemanlaı array olusturur
print(array)
print(array.max())  # max elemanı verir
print(array.min())  # min elemanı verir
array.sort()  # arrayi sıraar ve değişkilik kaydedilir
print(array)
print(array.mean())  # ortalama
print(array.sum())  # toplam
print(array.argmax())  # max elemann indisi verilir
print(array.min())  # min elemann indisi verilir
matris = np.random.randint(0, 10, (3, 3))
print(np.linalg.det(matris))  # determinant bulur
