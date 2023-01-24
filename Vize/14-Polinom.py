# x^2+2x+1
import random
liste = list()
for i in range(8):
    liste += [random.randrange(0, 20)]
for i in range(len(liste)):
    if i == 0:
        print(i, end="+")
    else:
        print(str(liste[i])+"x^"+str(i), end="+")
