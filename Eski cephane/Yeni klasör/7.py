#liste veri tipi
ogrenciler1=["ahmet","mehmet","salih","yasin"]
print(ogrenciler1)
print(ogrenciler1[1])
basaraliogrenciler=ogrenciler1[1:3]
print("basarali ogrenciler:",basaraliogrenciler)
print(ogrenciler1[::-1])
ogrenciler1[3]="muhammed"#ogrenci değiştirme
print(ogrenciler1)
print(type(ogrenciler1))
ogrenciler1.remove("salih")#ogrenci silme
print(ogrenciler1)
print(len(ogrenciler1))#boyut gösterir
yazi="mehmet"
yazi=list(yazi)
yazi[0]="k"
print(yazi)
ogrenciler2=["ayse","melis"]
ogrenciler=ogrenciler1+ogrenciler2#ekleme yapılabilir
print(ogrenciler)
liste=[1,2,3]
liste=liste*3#uc kere yazdırma sağlar
print(liste)
liste.append("ahmet")#listeye ekleme yapılır tipi farketmez
print(liste)
a=liste.pop()#en sondaki elamani çikarır popun içine indis girilirse indis çıkarılır
print(a)#çıkarılan elemani gösterir
print(liste)
liste.remove(2)#verilen elemani çıkarır
print(liste)
liste1=[15,889,44,8455,45,10]
liste1.sort(reverse=True)#listeyi siralar reverse true yapılırsa tersten sıralar
print(liste1)
kullanici=["maa","aaaa","alla"]
sifre=["1230","455","588"]
user=[kullanici,sifre]
for i in range(0,3):
    print("{}. inci kullanici adi: {}".format(str(i+1),user[0][i]), "{}inci. sifre: {}".format(str(i+1),user[1][i]), sep="\n",end="\n\n")
liste2= [["mehmet salih"],[1,2,3]] #liste içind eliste yapılabilir
print(liste2[0])
print(liste2[1])
print(liste2[1][2])
#set tekrar eden listedekileri tek e inidrger ve siralar
liste4=[1,2,1,2,2,4,5,7]
print(set(liste4))

