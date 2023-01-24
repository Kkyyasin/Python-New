def turkce_karekter_cevirici(metin):
    karekterler={"i":"ı","o":"ö","s":"ş","c":"ç","g":"ğ","u":"ü"}
    a=list(metin)
    for i in a:
        if i in karekterler:
           a[a.index(i)]=karekterler[i]
    return "".join(a)
print(turkce_karekter_cevirici("merhaba efendim yasasin"))
def sayi_yokedeci(metin):
    a=list()
    for i in metin:
       try:
         int(i)
       except:
        a.append(i)
    return  "".join(a)
print(sayi_yokedeci("11aa545444887845zzjzaj44"))
