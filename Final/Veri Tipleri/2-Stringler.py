import re
a = "Muhammed Yasin"

# len uzunluk bulur
print(len(a))

# replace karekter veya String ifade değiştirir
#!degistirir ama eşitlenmeli kendisine
print(a)
a = a.replace("a", "e")  # eski,yeni
print(a)

# split() içine girilen karektere gore ayır
print(a.split(" "))
print(re.split("\d+", "xkd456adjd"))  # buda regex ile ayırır
#Lower() and upper()
# Mutlaka karşılaşmışsınızdır. Bazı programlarda kullanıcıdan istenen veriler büyük-küçük harfe duyarlıdır. Yani mesela kullanıcıdan bir parola isteniyorsa, kullanıcının bu parolayı büyük-küçük harfe dikkat ederek yazması gerekir. Bu programlar açısından, örneğin ‘parola’ ve ‘Parola’ aynı kelimeler değildir. Mesela kullanıcının parolası ‘parola’ ise, bu kullanıcı programa ‘Parola’ yazarak giremez
c = "YASİN"
c = c.lower()  # ! esitlenmeli
print(c)
c = c.upper()  # ! esitlenmeli
print(c)
# capitalize sadece bas harf buyuk olur
c = c.capitalize()
print(c)
# swapcase buyuk harfi kucuk kucugu buyuk yapar
print(c.swapcase())

# endsiwith() ve startswith()
c = "Muhammed Yasin Ozdemir"
print(c.endswith("mir"))  # True sonuc alınır sonu kontrol eder
print(c.endswith("sin"))  # False alınır sonda değildir
print(c.startswith("Ya"))  # False
print(c.startswith("Mu"))  # True

#strip ,rstrip,lstrip

d = "     dsdsdıw  "
print(d)
print(d.strip())  # defaul bosluktur
print(d.rstrip())  # sağdakileri siler
print(d.lstrip())  # soldakileri siler
d = "xxxxxxxxxkkskodxxxxxxxx"
print(d.strip("x"))  # girilen karekteride siler

# Join listeyi donusturur stringe
f = ['Beşiktaş', "Jimnastik", "Kulübü"]
g = " ".join(f)

# count()  sayar harfi veya kaekter
# ? string içinde varmı kullanbailr index de cunku hata alırnır
print(g.count("e"))
print(g.count("ik"))

#index(), rindex()
# index bulur girilenin
print(g.index("k"))
print(g.rindex("k"))  # sondan baslar
print(g.index("a", 8))  # kacıncı sıradan

#find, rfind()
# bulur stringi bulamassa -1döndürür
print("Muhammed Yasin".find("h"))

print("Muhammed Yasin".find("jsaj"))
print("Muhammed Yasin".rfind("h"))
