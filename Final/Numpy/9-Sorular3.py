import numpy as np
arr1 = ((np.random.rand(9) * 5).astype(int)).reshape(3, 3)
arr2 = ((np.random.rand(9) * 5).astype(int)).reshape(3, 3)
print(arr1)
print(arr2)
# ?iki matrisi toplayın
print(arr1+arr2)
# ?iki matrisis çarpın
print(arr1*arr2)
# ?arr ortalama bulun elemanların
print(arr1.mean())
# ?arr1 matrisinin tüm elemanlarının toplamını bulun
print(arr1.sum())
