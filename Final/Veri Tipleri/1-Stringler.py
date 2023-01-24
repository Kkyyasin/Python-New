a = "Yasin"  # bu şekilde tanımlanır
a = "Muhammed Yasin"  # değişme ozelliği vardır

# input la alınan veri string doner
#!strngler a[0]="j" boyle bir sey olamaz anca replace ile
numara = "1234v56a78Ax"
toplam = 0
for i in numara:
    try:
        toplam += int(i)
    except ValueError:
        print(i+" donusemedi")
    finally:
        if numara.index(i) != len(numara)-1:
            print(numara[numara.index(i)+1] + " karektere geçildi...")
print("Toplam sonuc: {}".format(toplam))

# Stringlere erişim
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
    print("site: ", isim)
c = a[9:] + " Muhendis"  # ? 9 dahildir
print(c)
