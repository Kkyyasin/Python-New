import random
print(random.random())  # 1 0 arsaında rasgele sayı üretir
print(random.random()*10)
# girdiğimiz aralıkta rasgele sayı float değerli üretir
print(random.uniform(0.5, 10))
print(random.randint(10, 50))  # aralıkta tamsayı rasgele secer
print(random.choice(["ibi", "slld", 4, 8]))  # listeden rasgele seçer
# rasgele karıştıtıt
l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
random.shuffle(l)
print(l)
print(random.randrange(10))  # 0 10 arası ragele tam sayı üretir
# randintle aynı işi yapar ama buna tek paremtrede girebilirzi
print(random.randrange(5, 10))
