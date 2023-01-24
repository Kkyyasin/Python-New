a = "Muhammed Yasin"
print(a, "nın uzunlugu:", len(a))
# replace metodu harflerin yerlerini değiştirmeye yarar
b = "aauuaauu"
print(b)
# replace
"""Karakter dizisi metotları arasında inceleyeceğimiz ilk metot replace() metodu olacak. replace kelimesi Türkçede ‘değiştirmek, yerine koymak’ gibi anlamlar taşır. İşte bu metodun yerine getirdiği görev de tam olarak budur. Yani bu metodu kullanarak bir karakter dizisi içindeki karakterleri başka karakterlerle değiştirebileceğiz.
    """
b = b.replace("a", "e")  # eskideger,yenideger
print(b)  # eşitlemesen yer değiştirmiyor
a = a.replace("Ya", "Ta")  # tek karekter değil string de dğişebilir
print(a)  # !Dikkat kaydetmek isteniyorsa eşitlenmeli
b = "memleket"
print(b.replace("e", ""))  # siliyor gibi bos stringe eşitliyoy
print(b.replace("e", "", 1))  # sadece girdiğimiz sayı kadar girdi
# aslında kac tane varsa siler mantıgı var default yapar
print(b.replace("e", "", b.count("e")))

# split()
"""Bu metodun görevi karakter dizilerini belli noktalardan bölmektir. Zaten split kelimesi Türkçede ‘bölmek, ayırmak’ gibi anlamlara gelir. İşte bu metot, üzerine uygulandığı karakter dizilerini parçalarına ayırır. 
    """
İbb = "İstanbul Büyükşehir Belediyesi"
print(İbb.split())  # defaut olarak boslukla ayırır.
for i in İbb.split():
    print(i[0], end="")  # metnin bas harflerini alır ibb yazdırır.
sehirler = "Bolvadin, Kilis, Siverek, İskenderun, İstanbul"
print("\n", sehirler.split(","))  # virgule gore ayırır

#Lower() and upper()
# Mutlaka karşılaşmışsınızdır. Bazı programlarda kullanıcıdan istenen veriler büyük-küçük harfe duyarlıdır. Yani mesela kullanıcıdan bir parola isteniyorsa, kullanıcının bu parolayı büyük-küçük harfe dikkat ederek yazması gerekir. Bu programlar açısından, örneğin ‘parola’ ve ‘Parola’ aynı kelimeler değildir. Mesela kullanıcının parolası ‘parola’ ise, bu kullanıcı programa ‘Parola’ yazarak giremez
c = "YASİN"
c = c.lower()  # !eşitlenmeli
print(c)
c = c.upper()
print(c)
iller = "ISPARTA, ADIYAMAN, DİYARBAKIR, AYDIN, BALIKESİR, AĞRI"

iller = iller.replace("I", "ı").replace("İ", "i").lower()
print(iller)  # burda  ingiliz alfabesine gore düzenler
# capitalize sadece bas harf buyuk olur
c = c.capitalize()
print(c)
#endswith() and startswith()
# basını ve sonunu kontrol eder true false doner
print(c.endswith(c[-1:-3]))
print(c.startswith("Ya"))
print(c.startswith("qYa"))
# swapcase buyuk harfi kucuk kucugu buyuk yapar
print(c.swapcase())
#strip(), lstrip(), rstrip()
# gereksiz bosluk vs siler içine gireni belli kuarala gore siler
d = "     memme  "
print(d)
print(d.strip())  # defaul bosluktur
print(d.rstrip())  # sağdakileri siler
print(d.lstrip())  # soldakileri siler
# Join listeyi donusturur stringe
f = ['Beşiktaş', "Jimnastik", "Kulübü"]
g = " ".join(f)
print(g)
# count()  sayar harfi veya kaekter
print(g.count("e"))
print(g.count("ik"))
#index(), rindex()
# index bulur girilenin
print(g.index("k"))
print(g.rindex("k"))  # sondan baslar
print(g.index("a", 8))  # kacıncı sıradan itibaren baslamasını belirtiziz
#find, rfind()
# bulur stringi bulamassa -1döndürür
