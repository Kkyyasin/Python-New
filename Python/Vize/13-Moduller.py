import kendimodul
import random
print(random.random())  # 0 ile 1 arsaında float değer olusturur
print(random.random()*10)  # 0 10
print(int(random.random()*10))
print(random.randrange(1, 10))  # bu daha iyiy
print(random.randint(1, 10))
liste = ['ali', 'veli', 'ahmet',
         'mehmet', 'celal', 'selin', 'nihat']
print(random.choice(liste))  # rasgele secer
print(random.shuffle(liste))  # listeyi karıştırır
kendimodul.ara("aas")
kendimodul.ara("kitap")
