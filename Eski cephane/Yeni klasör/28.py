while True:
    try:
        boy=float(input("boyunuzu giriniz:"))
        break
    except ValueError:# istenilen hatada eror verir
        print("boy hatali")
while True:
    try:
        kilo=float(input("kilo giriniz:"))
        break
    except:#her hatada eror verir
        print("kilo hatali")
print("boy kilo indeski:{}".format(kilo/boy**2))
def sayilaritopla(sayilar):
    if type(sayilar) !=list():
        raise TypeError("liste objesi değil")
    toplam=0
    for i  in sayilar:
        toplam+=i
    return toplam
try :
 print(sayilaritopla("nee"))
except:
    print("buraya girdi")