#random modulu
import random
import math
print(random.random())#(0,1) arası rasgele değer dondurr
print(random.randint(1,12))#girilen sayı arsında ssyı tutar
print(random.uniform(1,9))#girilen sayı arsında float değer utar
print(random.choice(range(0,100)))#girilen listed rasgele değer dondurur
print(random.sample(range(0,20),k=3))#3 tane listeden rasgele değer donduru
a=[*range(0,10)]
print(a)
random.shuffle(a)#listeyi ragele sıralamaya yarar
print(a)
import math
print(round(7.1))
print(round(7.7))#yuvarlamaya yarar
print(math.ceil(7.1))#her zaman uste yuvarlar
print(math.floor(7.7))#her zaman alta yuvarlar
print(math.factorial(5))#faktoreyel alır
print(math.pow(3,4))#us alır
