import numpy as np
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]
                  )
print(array.ndim)  # boyutu verir
# elemanlara erişme array
# listelerdekine benzer erişimi vardır
print(array[0])  # 0 indise erişim sağlanır
print(array[3])  # 3 indise erişim sağlanır
print(array[:2])  # 2 indise kadar elemanları verir
#!2 dahil değil
print(array[1:4])  # 1 ve 4 e kadar elamanlara erişim sağlanır
#!1 dahil 4 değil
print(array[::2])  # ikişer ikişer atlayarak erişim sağlanır
try:
    print(array[11])
except IndexError:
    print("IndexError hatası...")

# Çok boyutlu elemanara erişme
# farklı bir yapısıs vardır koordinat duzlemine benzer
print(array2[1, 2])  # 2 satır 3 sutune erişim sağlanır
print(array2[:, 1])  # tüm satırlardaki 2 sutunları verir
print(array2[1, :])  # 2 satırır yazdırır
print(array2[:2, :])  # 2 satıra kadar yazdırı
print(array2[:2, :3])  # 2 satır 3 sutuna kadar yazdırır
# 1 ve 3 sutun arasındaki 2 ve 4 sutun arası elemanları alır
print(array2[1:3, 2:4])
# ? Yapı array2[satır aralığı,sutun aralığı] yapı liste yapısı array aynı metot
# 2 den fazla boyutlu erişim
array3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], [[
                  1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]])
print(array3[1, 0, 1])  # indisleme bıyle olur dıstan içeri dogru
