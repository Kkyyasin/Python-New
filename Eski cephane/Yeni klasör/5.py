dosya=open("metin belgesi.txt","w")
print("merhaba","efendim",file=dosya)#file yapılır
dosya2=open("metinbelgesi3.txt","w")
a="merhaba"
print(5*"a\n",file=dosya2)
isim="ahmet"
soyad="özdemir"
numara=125
dosya3=open("kisi bilgisi.txt","w")
print("isim:%s"%(isim),"soyad:{}".format(soyad),"numara:{}".format(str(numara)),sep="\n",file=dosya3)
dosya.close()