#sqlite veri tabani
from sqlite3 import *
baglanti=connect("veri tabani1.db")#veri tabanina bağlanmayı sağlar
imlec=baglanti.cursor()
imlec.execute("CREATE TABLE IF NOT EXISTS uyeler(İsim TEXT,Yas INT,Cinsiyet TEXT)")

imlec.execute("INSERT INTO uyeler VALUES('selin',18,'kiz')")
imlec.execute("INSERT INTO uyeler VALUES('zeynep',17,'kiz')")#veri ekleme sağlar
imlec.execute("INSERT INTO uyeler VALUES('mustafa',19,'erkek')")
baglanti.commit()
baglanti.close()