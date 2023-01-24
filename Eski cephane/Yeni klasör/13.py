#and ve dir or veyadır
#ogrenci not hesaplayici
dosya=open("not.txt","a")#a olursa uzerine ekleme yapar
kisi=input("isim soyisim giriniz:")
vize=float(input("vize notunu giriniz:"))
final=float(input("final notunu giriniz:"))
basarınotu=0.4*vize+0.6*final
print("{} ogrencini basari notu:{}\nHarf notu:".format(kisi,basarınotu),file=dosya,end="")
if 100>basarınotu and 85<basarınotu:
    print("AA",file=dosya)
elif 85>basarınotu and 70<basarınotu:
    print("BB",file=dosya)
elif 70>basarınotu and 55<basarınotu:
    print("CC",file=dosya)
elif 55>basarınotu and 35<basarınotu:
    print("CC",file=dosya)
elif 35>basarınotu and 0<basarınotu:
    print("DD",file=dosya)
else:print("hatali not girişi")

dosya.close()

