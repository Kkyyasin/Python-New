import numpy as np
# ?10x10 matris olustur 1 den 100 kadar
m = np.arange(1, 101).reshape(10, 10)
print(m)
# ?40 dan buyukleri al
print(m[m > 40])
# ?son 6 ve son 5 satur sutun al
print(m[6:, 4:])
"""array([[ 3,  4],
       [13, 14],
       [23, 24]])
       """
print(m[:3, 2:4])  # !satır sutun yerlerine dikkat et satır ilk basta sutun sonrası
"""
array([ 2, 12, 22])
"""
print(m[:3, 1])
"""array([ 10,  20,  30,  40,  50,  60,  70,  80,  90, 100])"""
print(m[:, -1])
