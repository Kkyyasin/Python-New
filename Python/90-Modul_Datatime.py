from datetime import date, datetime
import locale
from this import d

# suanki yeri belirtiyoz içine birşey girilmesse ve tarih vs turkce oluyor
locale.setlocale(locale.LC_ALL, "")
# zaman tarih işlemlerinde kullanılır.
print(datetime.now())
su_an = datetime.now()
print(su_an.day)
print(su_an.year)  # bunlar gibi suanın zaman bilgileri tek tek alınır
print(su_an.month)
print(su_an.time())  # saat
print(su_an.time().minute)  # dakika
# ctime daha guzle gorunur
print(datetime.now().ctime())
# strftime ozel komutlarla tek tek alınır
print(datetime.strftime(su_an, "%Y"))  # yıl
print(datetime.strftime(su_an, "%B"))  # AY
print(datetime.strftime(su_an, "%d"))  # gun
print(datetime.strftime(su_an, "%d/%B/%Y"))  # yan yana yazmaya %d gunyarar

# timestamp() suanki zamani saniyeye cevirir fromtimestamp saniyeye datetime ceviryor
su_an2 = datetime.now()
sn = su_an2.timestamp()
su_an3 = datetime.fromtimestamp(sn)
print(sn)
print(su_an3)
print(datetime.fromtimestamp(0))  # milad 1970

# tarih olusturma
tarih = datetime(2003, 7, 18)  # yıl ay gun
suan = datetime.now()
birtday = suan-tarih
print(birtday)
print(birtday.days)
print(birtday.days//365, "Yaş")
