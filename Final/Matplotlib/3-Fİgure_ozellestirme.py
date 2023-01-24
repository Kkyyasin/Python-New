import matplotlib.pyplot as plt
import numpy as np
x = np.arange(1, 6)
y = np.arange(3, 18, 3)
# 4 grafik olusturur 2 satır 2 sutn halinde figurileri ve axex leri donus tipi olarak verir
fig, axes = plt.subplots(nrows=2, ncols=2)
axes[0, 0].plot(x, y)
axes[0, 1].plot(y, x)
plt.show()
