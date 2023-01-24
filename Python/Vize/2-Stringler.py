a = "Yasin"  # String boyle tanımlanıyor
x = 'boylede olabilir'
y = """
boyle de olabilri"""
print(a)
a = "Muhammed Yasin"  # değişebilir
#!strngler a[0]="j" boyle bir sey olamaz anca replace ile
print(a)
b = input("Giriş:")  # inputtan alınan veri string doner
print(b)
for i in a:  # her i değeri bir karekteri alır
    print(i, end=" - ")  # karekterleri yazdırırz
print()
nesne = "123456789"
for n in nesne:  # meselam burda sayı yı string alıp int donusturup 2 ile çarptık
    print(int(n) * 2, end="   ")

# String erişim sağlama
print(a[0])  # ilk indise erişiriz
print(a[2:])  # 2 indisten başlayıp son indise erişiriz
print(a[::2])  # ikişer sekilde atlayarak yazdırır

print(a[-1::-1])  # sondan yazdırırz -1 son elemanı temsil eder
print(a[-1:-(len(a)+1):-1])  # sondan yazdırma ikinci yol
print(a[::-1])  # sondan yazdırma en mantıklı yol

print(a[len(a)-1])  # son elemanı temsil eder
print(a[-1])  # ikinci yol son elemanı bulma
site1 = "www.google.com"
site2 = "www.istihza.com"
site3 = "www.yahoo.com"
site4 = "www.gnu.org"

for isim in site1, site2, site3, site4:  # siteleri bu kullanım ile liste gibi kullanmaya yarar
    # .com ları ile www. ları almayarak google vs yazırmaya yara
    print("site: ", isim[4:-4])

# String işlemler
print("merhaba"+"Yasin")  # bosluksuz yazar
c = a+" Komutan"
print(c)
# !Önemliiiiiiiiiiii Burada 9 dahil o yuzden neyi yazdırmak isteniyorsa o harfin indisi yazılır
d = a[9:]+" "+"Komutan"
print(d)
sesli_harfler = "aeıioöuü"
sessiz_harfler = "bcçdfgğhjklmnprsştvyz"

sesliler = ""
sessizler = ""

kelime = "istanbul"

for i in kelime:
    if i in sesli_harfler:
        sesliler += i  # karekterler kopyalanıyor
    else:
        sessizler += i

print("sesli harfler: ", sesliler)
print("sessiz harfler: ", sessizler)
# gloabal deyimi
x = 0


def fonk():
    x = 1
    print(x)


fonk()
