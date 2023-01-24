import numpy as np
array = np.arange(20, 30)
array2 = np.arange(10)
# array toplama
print(array+array2)
print(array-array2)
print(array*array2)
print(array-2)
print(array+5)
print(array*4)
print(np.sqrt(array))  # karekok alır
# Matris işlemleri
m1 = np.arange(1, 5)
m2 = np.arange(4, 8)
print(np.dot(m1, m2))  # matrisleri çarpar

print(m1.T)  # Tranpoze alır satur sutun sutun satır olur
print(m1.shape)  # satır ve sutun yerini
