#map sınıfı
def kareal(x):
    return x**2
a=[1,2,3,4]
print(*map(kareal,a),sep="  ")
print(list(map(kareal,a)))
user={
    "myasim":"22222",
    "skxsk":"445",
    "sss":"555"
}
def kontrol(username,pasapord):
  try:
      if user[username]==pasapord:
          return True
      else:
          return False
  except:
      return  False
result=list(map(kontrol,["myasim","asa","sss"],["22222","445","554"]))
print(*result)
#max min sum fonksiyonu
print(max(1,55,45))#maxı verir liste de olabilir
print(min([11,55,1.2]))#mini verir
print(sum([45,54,47,5.4]))#girilenleri toplar
#zip
isim=["mee","aaa","ss"]#birleştirir aynı karaekter sayisi olmali
yas=[18,88,24]
print(list(zip(isim,yas)))
for ad,yas in zip(isim,yas):
    print("isim:{}\nyas:{}".format(ad,yas))
#enumarte
print(list(enumerate(isim,1)))#1 baslangiç değeri verir
for i,isim in enumerate(isim,1):
    print("{}-{}".format(i,isim))