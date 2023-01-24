import datetime as t  # tarih ve saatle ilgili işlemleri yapar
an = t.datetime.now()  # şimdiki zamanı yazar datatime sınıfından
print(an)  # hepsi
print(an.year)  # yıl
print(an.month)  # ay  biligileir boyle tek tek alabiliriz
print(an.day)  # güm
print(an.hour)  # saat
print(an.minute)  # dakika
print(an.second)  # saniye
an = t.datetime.today()  # now la aynı işi yapr
print(an)
tarih = t.datetime.ctime(an)
print(tarih)  # tarih okunuşları yazar
