import numpy as np
array = np.arange(1, 20, 2)
print(array[::2])
print(array[1:5])
# eleman değiştirme
print(array)
array[6] = 32
print(array)
array[:4] = 24  # 4 e kadar 24 yapar
array2 = array  # refereans veriri deger ikiside değişir
array2[8] = 12
print(array)
array3 = array.copy()  # refereans vermez değerlerle yeni olusturur
array3[0] = 12
print(array)
print(array3)
array = np.arange(10)
# matris haline çevirme reshape
print(array.reshape(5, 2))  # eleman sayısı satır sutun carpına eşit olmalı
arr = array.reshape(2, 5)
print(arr)
print(arr[:, :2])  # butun satırlardaki 1 ve 2 sutunu alır

# ?Array Filtreleme
print(arr > 3)  # boolean array dondurur
print(arr[arr > 3])  # arraye göre filtreler false aturlır truelear kalırr
