# paremetreler
# 1-normal paremetre
def kucukbul(a, b):  # a ve b normal paremetre
    if a < b:
        return a
    else:
        return b


print(kucukbul(12, 56))
# ?2-liste objesi gibi istediği kadar alma *degisken ile yapılır


def topla(*sayilar):  # liste objesi gibi alır
   toplam = 0
   for i in sayilar:
        toplam += i
   return toplam
print(topla(12, 25, 24,2))#istediği kadar sayi alır
#3-sabit yapma default
def usal(a,b=2):
    return a**b
print(usal(2))#otamatik b değeri alır
print(usal(2,3))#girilen değeri alır printdeki end sep gibi
#4-**değişkenler sozluk gibi alır yani dick yapısı gibi
def a(**degiskenler):
    for sarki,sanatci in degiskenler.items():
        print(">sarki : {}\n>sanatcisi : {}".format(sarki,sanatci),end="\n--------\n")
    for i in degiskenler:
        print(i)
a(dolunay="reymen",kul="cem adrian")#birincisi değişkeni ikincisi neye seti oldugu