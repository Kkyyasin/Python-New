import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 6)
y = np.arange(3, 18, 3)
fig = plt.figure()  # figure olusturur
# figure penceredir
axes1 = fig.add_axes([0.1, 0.2, 0.3, 0.3])  # 0 ile 1 arası degerler verilir
# sırasıyla paremetreler x ekseni ,y ekseni ,yatay uzunluk ,dikey uzunluk
axes1.plot(x, y, color="red")  # grafik .izer
axes1.set_xlabel("X Label")
axes1.set_ylabel("Y Label")
axes1.set_title("Title")
axes2 = fig.add_axes([0.5, 0.4, 0.4, 0.4])
axes2.plot(y, x, color="purple")
plt.show()
