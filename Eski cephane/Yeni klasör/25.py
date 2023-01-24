#moduller importla cagrilir
import random as m#as kelimesi c deki yype gibi ismi değiştiriyor
a=m.randint(1,100)#girilen aralıkta değer tutar
b=("mehab","xs",True,5,87)
c=m.choice(b)#girilen listede veya tupplede rassgele birini secer
print(c)
print(a)
import hesapmakinesi1#fonksiyon boyle cagrılabilmesi icin basa adı ayzılır
print(hesapmakinesi1.topla(4,2))
print(hesapmakinesi1.cıkar(4,2))
print(hesapmakinesi1.carp(4,2))
print(hesapmakinesi1.bol(4,2))
import math
print(help(math.ceil))#fonksiyomları gosterir kutuphanede . ile bişey yazılırsa fonksiyo açıklaması yazar ceil yuvarlama yapar
print(math.ceil(3.14))
from hesapmakinesi2 import*#fonksiyonun hepsini çağırır print gibi olur hesapmakinesi2 yazmaya gerek kalmaz *yerine foksiyon isimleri yazlırsa (topla,cıkarma)ozel olarak yazılanları çıkarır sadece
print(topla(7,8))
print(cıkar(7,8))
print(carp(7,8))
print(bol(7,8))
#as isim değişikliği yapar
from builtins import print as yazdir
yazdir("merhaba")#print fonksiyonu boyle ismi değişir
from builtins import int as tamsayi
print(tamsayi(3.14))


