import datetime
from datetime import *
print(date.today())#bugunun tariğini verir
a=date(2021,4,6)#kendi tariğimiz olustururuz
print(a)
yas=date.today().year-date(2003,7,18).year
print(yas)
yarın=date.today()+timedelta(days=1)#bir gün ekleme işlemi
print(yarın)
print(date.weekday(a))#haftanın kacıncı gunu olduğunu soyler
print(date.ctime(a))
zaman=time(20,15,25)#20 saat 15 dakika25 saniyedir
print(zaman)
print(zaman.hour)
print(zaman.minute)
print(zaman.second)
a=datetime(2020,4,11,21,10,45)
print(a)
print(a.hour)
print(a.minute)
print(a.second)
print(a.year)
print(a.month)
print(a.day)
import  time
bas=time.time()
print(bas)
time.sleep(3)
bit=time.time()
print(bit)
print(bit-bas)
print(round(bit-bas))