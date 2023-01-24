#print ozellikleri
print("merhaba"+"merha")#string toplamsı yapar birlşeik yazar
print("merhaba","merhaba")#ayrı ayrı alır
a=5
b=7
print(a+b)#burda toplama yapar
print(a,b)#burda ayrı ayrı yazdırır
print("merh",a)#int ile string ifade virgülle birleşir sadece
print("merhaba\ndunya")#\n asağı geçmeye yarar
print("merhaba\tdunya")#bosluk bırakır
x=4
y="aaa"
z=True
print(type(x),type(z),type(y))#veri tipleri ogrenmek için kullanılır
print(a,b,x,sep="aa")#her adım arası yazılanı bırakır otomatik boşluk bırakır
def islem(sayi,yapi):
    if yapi=="+":
        return sayi+sayi
    else:
        return sayi*sayi
print(islem(4, "*"))
print(x,end="--")#end sonda ne yaptığını beliler değişmezse gizli\n vardir
print(x)
print(*y)#indisler ayrilir
isim="yasin"
print("merhaba {} efendim".format(isim),end="\n--\n")#{} araya string ifade koymaya yarar.
print("merhaba %s"%(isim))#%s formatla aynı görevi görür.
