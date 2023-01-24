import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 6)
y = np.arange(3, 18, 3)
print(x, y, sep="\n")
plt.plot(x, y, "red")  # xduzlemi,y duzlemi,grafik çizgi rengi
# Grafikleri bir çok olustrma pencerede
plt.show()
plt.subplot(2, 2, 1)
plt.plot(x, y)  # otomatik renk atar
plt.subplot(2, 2, 2)
plt.plot(y, x)
plt.subplot(2, 2, 3)
plt.plot(x, x**2)
plt.subplot(2, 2, 4)
plt.plot(y, y**2)
plt.show()
